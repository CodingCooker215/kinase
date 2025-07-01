import pandas as pd

# Dictionary for 3-letter to 1-letter amino acid conversion
AA_CODE = {
    'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C',
    'GLN': 'Q', 'GLU': 'E', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I',
    'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F', 'PRO': 'P',
    'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V',
    'SEC': 'U', 'PYL': 'O', 'ASX': 'B', 'GLX': 'Z', 'XAA': 'X',
    'XLE': 'J', 'TERM': '*'
}

df=pd.read_csv("pdbanalysis/4af3_seq.csv")
df_unique = df.drop_duplicates()
df_unique.columns=["amino acid", "pos"]
df_unique['1-letter'] = df_unique['amino acid'].map(AA_CODE)
df_unique.to_csv("processed_seq.csv")