import os
import subprocess
import numpy as np
import PDBparser as pdbp
import PDBmanip as pdbm

pdbs = {}
with open("PDBsToCheck.txt", "r") as inData:
    for line in inData:
        line = line.strip()
        pdbs[line[0:4]] = line[5]
print(pdbs)

pdbp.download_pdbs(list(pdbs.keys()), output_path = "CompPDBs/")

for key in pdbs:
    pdbm.one_chain_pdb("CompPDBs/%s.pdb"%key, key, chainID = pdbs[key], remove_tags = False)

with open("PDBsToCheck_NoChain.txt", "w+") as outData:
    outData.write("\n".join(list(pdbs.keys())))
