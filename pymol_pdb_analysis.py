curr_pdb=[]
data=[]
filely=open("aukb_wt_128_256_alignment_DFG.txt", "w")

#DFG=142-144
#G_Loop=8-13
#aC=43-53


def stripy(name, prefix, suffix):
    # Remove the prefix
    if name.startswith(prefix):
        name = name[len(prefix):]
    # Remove the suffix
    if name.endswith(suffix):
        name = name[:-len(suffix)]
    return name.strip('/')  # Remove any leading/trailing slashes

with open("aukb_domain_wt_128_256.txt", "r") as f:
    lines=f.readlines()
    for j in lines:
        curr_pdb.append("/Users/jasonhwang/Documents/Brown/Rubenstein/aukb_domain_wt_128_256/"+j.strip())

# cmd.load("AukB_G_Loop.pdb")
# cmd.color_deep("red", "AukB_G_Loop", 0)
def annoatate():
    cmd.select("DFG", "resi 142-144")
    cmd.color_deep("Green", "DFG")
    cmd.set("cartoon_transparency", 0, "DFG")

    cmd.select("G_Loop", "resi 8-13")
    cmd.color_deep("Blue", "G_Loop")
    cmd.set("cartoon_transparency", 0, "G_Loop")


    cmd.select("aC_helix", "resi 43-53")
    cmd.color_deep("Wheat", "aC_helix")
    cmd.set("cartoon_transparency", 0, "aC_helix")


    cmd.select("F219", "resi 143")
    cmd.show("sticks", "F219")
    cmd.color_deep("pink", "F219")
    cmd.set("cartoon_transparency", 0, "F219")

def DFG():
    for i in range(len(curr_pdb)):
        print(i)
        cmd.load("AukB_DFG.pdb")
        cmd.color_deep("red", "AukB_DFG", 0)
        paths=f"{curr_pdb[i]}"
        cmd.load(paths)
        cleaned_name = stripy(paths, "/Users/jasonhwang/Documents/Brown/Rubenstein/aukb_domain_wt_128_256/", ".pdb")
        cmd.color_deep("white", f'{cleaned_name}', 0)
        cmd.set("cartoon_transparency", 0.75, f"{cleaned_name}")
        annoatate()
        curr_data=cmd.align("polymer and name CA and (AukB_DFG)","polymer and name CA and (DFG)",quiet=0,object="aln_AukB_DFG_to_DFG",reset=1)
        data.append(f"{cleaned_name}|{curr_data} \n")
        cmd.center()
        cmd.set_view((
      0.364821821,    0.235291421,    0.900856614,
     0.666502714,    0.609603405,   -0.429134250,
    -0.650137544,    0.756981492,    0.065574400,
     0.000000000,    0.000000000, -187.763702393,
     1.059869766,   -1.174396515,    1.122215271,
  -6261.794921875, 6637.324707031,  -20.000000000 ))
        cmd.png(f"/Users/jasonhwang/Documents/Brown/Rubenstein/pdbtest/{cleaned_name}_DFG_test2", 0, 0, -1, ray=0)
        cmd.delete("all")
def G_Loop():
    for i in range(len(curr_pdb)):
        cmd.load("AukB_G_Loop.pdb")
        cmd.color_deep("red", "AukB_G_Loop", 0)
        paths=f"{curr_pdb[i]}"
        cmd.load(paths)
        cleaned_name = stripy(paths, "/Users/jasonhwang/Documents/Brown/Rubenstein/aukb_domain_wt_128_256/", ".pdb")
        #cmd.color_deep("yellow", f'{cleaned_name}', 0)
        annoatate()
        curr_data=cmd.align("polymer and name CA and (AukB_G_Loop)","polymer and name CA and (AukB_G_Loop)",quiet=0,object="aln_AukB_G_Loop_to_G_Loop",reset=1)
        data.append(f"{cleaned_name}|{curr_data} \n")
        cmd.png(f"/Users/jasonhwang/Documents/Brown/Rubenstein/pdb/{cleaned_name}_DFG", 0, 0, -1, ray=0)
        cmd.delete("all")

DFG()

print(data)
for lines in data:
    filely.write(lines)
