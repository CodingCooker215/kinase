def annoatate():
    cmd.select("DFG", "resi 142-144")
    cmd.color_deep("Green", "DFG")
    cmd.select("G_Loop", "resi 8-13")
    cmd.color_deep("Blue", "G_Loop")
    cmd.select("aC_helix", "resi 43-53")
    cmd.color_deep("Wheat", "aC_helix")
    cmd.select("F219", "resi 143")
    cmd.show("sticks", "F219")
    cmd.color_deep("pink", "F219")

paths="aukb_domain_wt_128_256/aukb_domain_wt_unrelaxed_rank_007_alphafold2_ptm_model_4_seed_001.pdb"
cmd.load("AukB_DFG.pdb")
cmd.color_deep("red", "AukB_DFG", 0)
cmd.load(paths)
cmd.color_deep("white", "aukb_domain_wt_128_256/aukb_domain_wt_unrelaxed_rank_007_alphafold2_ptm_model_4_seed_001", 0)
annoatate()
curr_data=cmd.align("polymer and name CA and (AukB_DFG)","polymer and name CA and (DFG)",quiet=0,object="aln_AukB_DFG_to_DFG",reset=1)
cmd.center()

cmd.set_view ((
     0.920992672,    0.253779471,    0.295576155,
    -0.047541913,   -0.679826796,    0.731826901,
     0.386661768,   -0.688062787,   -0.614052534,
     0.000043593,   -0.000026725, -100.996780396,
   -14.019298553,   -0.482840061,    5.534012794,
  -52286.097656250, 52488.082031250,  -20.000000000 ))