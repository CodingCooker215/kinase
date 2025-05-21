#note this is for analysing sim v orgin

#4AF3 is AurkB complex with INCENP and VX680 
#VX680 is aurkB inhibitor while INCENP is centromer prtein
keep=""
cookies=[]
best=float(0)

cookies.append("/Users/jasonhwang/Downloads/aurkb_unrelaxed_rank_004_alphafold2_ptm_model_2_seed_020.pdb")
cookies.append("/Users/jasonhwang/Downloads/aurkb_unrelaxed_rank_003_alphafold2_ptm_model_1_seed_007.pdb")
cookies.append("/Users/jasonhwang/Downloads/aurkb_unrelaxed_rank_002_alphafold2_ptm_model_4_seed_021.pdb")
cookies.append("/Users/jasonhwang/Downloads/aurkb_unrelaxed_rank_001_alphafold2_ptm_model_1_seed_021.pdb")

def stripy(name, prefix, suffix):
    # Remove the prefix
    if name.startswith(prefix):
        name = name[len(prefix):]
    # Remove the suffix
    if name.endswith(suffix):
        name = name[:-len(suffix)]
    return name.strip('/')  # Remove any leading/trailing slashes

cmd.fetch("4AF3")
cmd.util.cbc()
cmd.hide("/4AF3/E/D")
cmd.hide("/4AF3/B/D")
cmd.color_deep("orange", '4AF3', 0)

for path in cookies:
    cmd.load(path)
    cleaned_name = stripy(path, "/Users/jasonhwang/Downloads", ".pdb")
    curr_data=cmd.align("4AF3", f"{cleaned_name}")
    rmsd_val=float(curr_data[0])
    print(rmsd_val)
    if rmsd_val>=best:
        best=rmsd_val
        keep=cleaned_name
    cmd.hide("everything",cleaned_name)
cmd.show("cartoon", keep)