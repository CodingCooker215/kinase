import os
abs_path="/Users/jasonhwang/Documents/Brown/Rubenstein/aukb_domain_wt_128_256"
f=open("aukb_domain_wt_128_256.txt", "w")

PDB=[]
for files in os.listdir(abs_path):
    if files.endswith("pdb"):
        PDB.append(files)
        f.write(f"{files}\n")

print("complete")

