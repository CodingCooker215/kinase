import os
abs_path="/Users/jasonhwang/Documents/Brown/Rubenstein/aukb_domain_t232d_64_128"
f=open("aukb_domain_t232d_64_128.txt", "w")

PDB=[]
for files in os.listdir(abs_path):
    if files.endswith("pdb"):
        PDB.append(files)
        f.write(f"{files}\n")

print("complete")

