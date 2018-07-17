import os
import re
import glob

all_barrels = {}
with open("BarrelChars85.txt", "r") as barrel_data:
  for line in barrel_data:
    if "PDB" not in line:
      line = line.strip().split()
      all_barrels[line[0]] = int(line[1])

all_homologues = {}
for filename in glob.glob("MSAs/*.a3m"):
    pdb_id = filename.split("/")[-1][:-4]
    pdb_id = pdb_id[0:4].lower() + pdb_id[4:]
    a3m_list = []
    with open(filename, "r") as inData:
        for line in inData:
            if ">tr|" in line:
                new_id = line.split("|")[1]
                a3m_list.append(new_id)
    all_homologues[ pdb_id ] = a3m_list

with open("data/AllDataE1_v6_Numbered.txt", "r") as inData, open("data/AllDataE1_v6_Numbered_Hom.txt", "w+") as outData, open("data/AllDataE1_v6_Numbered_Hom_Tabbed.txt", "w+") as outDataTab:
    for line in inData:
        line = line.strip().split(" ")
        pdb1 = line[1]
        pdb2 = line[2]
        
        if pdb1 in all_barrels.keys() and pdb2 in all_barrels.keys():
            all_homos = len(set(all_homologues[pdb1] + all_homologues[pdb2]))
            shared_homos = len(set(all_homologues[pdb1]).intersection(all_homologues[pdb2]))
            #print(pdb1, pdb2, shared_homos/all_homos)
            outData.write(" ".join(line) + " " + str(shared_homos/all_homos) + " "+ str(all_homos) + "\n")
            outDataTab.write("\t".join(line) + "\t" + str(shared_homos/all_homos) + "\t" + str(all_homos) + "\n")
        else:
            outData.write(" ".join(line) + " 0 0\n")
            outDataTab.write("\t".join(line) + "\t0\t0\n")
            