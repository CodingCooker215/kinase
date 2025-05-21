#note this is for analysing sim v orgin

#4AF3 is AurkB complex with INCENP and VX680 
#VX680 is aurkB inhibitor while INCENP is centromer prtein

keep=""
cookies=[]
best=float(0)

#put in location of generated PDB files from fastconf
cookies.append("/Users/jasonhwang/Downloads/aurkb_unrelaxed_rank_004_alphafold2_ptm_model_2_seed_020.pdb")
cookies.append("/Users/jasonhwang/Downloads/aurkb_unrelaxed_rank_003_alphafold2_ptm_model_1_seed_007.pdb")
cookies.append("/Users/jasonhwang/Downloads/aurkb_unrelaxed_rank_002_alphafold2_ptm_model_4_seed_021.pdb")
cookies.append("/Users/jasonhwang/Downloads/aurkb_unrelaxed_rank_001_alphafold2_ptm_model_1_seed_021.pdb")

#this processes file name
def stripy(name, prefix, suffix):
    # Remove the prefix
    if name.startswith(prefix):
        name = name[len(prefix):]
    # Remove the suffix
    if name.endswith(suffix):
        name = name[:-len(suffix)]
    return name.strip('/')  # Remove any leading/trailing slashes

#adds and organizes template
cmd.fetch("4AF3")
cmd.util.cbc()
cmd.hide("/4AF3/E/D")
cmd.hide("/4AF3/B/D")
cmd.color_deep("orange", '4AF3', 0)

#adds and compares generated with template
for path in cookies:
    cmd.load(path)
    cleaned_name = stripy(path, "/Users/jasonhwang/Downloads", ".pdb")
    curr_data=cmd.align("4AF3", f"{cleaned_name}")
    rmsd_val=float(curr_data[0])
    cmd.png(f"/Users/jasonhwang/Documents/Brown/Rubenstein/pdbanalysis/{cleaned_name}_4AF3", 0, 0, -1, ray=0)
    if rmsd_val>=best:
        best=rmsd_val
        keep=cleaned_name
    cmd.hide("everything",cleaned_name)

#shows best alignment
print(best)
cmd.show("cartoon", keep)