#need to identify DFG and GXGXXG loop in generated predicitons, then align based on sequence


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
    cmd.select("G_Loop", "resi 8-13")
    cmd.color_deep("Blue", "G_Loop")
    cmd.select("aC_helix", "resi 43-53")
    cmd.color_deep("Wheat", "aC_helix")
def DFG():
    for i in range(len(curr_pdb)):
        cmd.load("AukB_DFG.pdb")
        cmd.color_deep("red", "AukB_DFG", 0)
        paths=f"{curr_pdb[i]}"
        cmd.load(paths)
        cleaned_name = stripy(paths, "/Users/jasonhwang/Documents/Brown/Rubenstein/aukb_domain_wt_128_256/", ".pdb")
        #cmd.color_deep("yellow", f'{cleaned_name}', 0)
        annoatate()
        curr_data=cmd.align("polymer and name CA and (AukB_DFG)","polymer and name CA and (DFG)",quiet=0,object="aln_AukB_DFG_to_DFG",reset=1)
        data.append(f"{cleaned_name}|{curr_data} \n")
        cmd.png(f"/Users/jasonhwang/Documents/Brown/Rubenstein/pdb/{cleaned_name}_DFG", 0, 0, -1, ray=0)
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



print(data)
for lines in data:
    filely.write(lines)
    