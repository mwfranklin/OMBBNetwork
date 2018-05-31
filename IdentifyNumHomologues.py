import os
import re
import glob

cutoff = 1e-10

prototypicals = []
with open("CompCodesE<1.txt", "r") as inData:
    for line in inData:
        if "PDB" not in line:
            line = line.strip().split("\t")
            if line[1] == "1": prototypicals.append(line[0].upper())

all_hits = []
for filename in glob.glob("MSAs/*.a3m"):
    pdb_id = filename.split("/")[-1][:-4]
    a3m_list = []
    if pdb_id in prototypicals:
        with open(filename, "r") as inData:
            for line in inData:
                if ">tr|" in line:
                    new_id = line.split("|")[1]
                    a3m_list.append(new_id)
        all_hits.extend(a3m_list)

print(len(all_hits), len(set(all_hits)))