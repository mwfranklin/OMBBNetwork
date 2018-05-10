import re
import glob
import sys

protos = []
with open("CompCodesE<1.txt", "r") as barrel_codes:
    for line in barrel_codes:
        line = line.strip().split("\t")
        if line[1] == "1":
            protos.append(line[0])

barrel_sizes = {}
needed_barrels = []
with open("BarrelChars85.txt", "r") as barrel_data:
    for line in barrel_data:
        if "PDB" not in line:
            line = line.split("\t")
            barrel_sizes[line[0]] = int(line[1])
            if int(line[1]) == 16 or int(line[1]) == 18:
                if line[0] in protos: needed_barrels.append(line[0])

with open("AllData_E20.txt", "r") as inData, open("16_18DataOnly.txt", "w+") as subnetwork:
    for line in inData:
        if "Dom1" in line:
            subnetwork.write(line)
        else:
            line = line.strip().split("\t")
            pdb1 = line[0]
            pdb2 = line[1]
            
            if pdb1 in needed_barrels and pdb2 in needed_barrels and float(line[2]) <= 1e-2:
                if barrel_sizes[pdb1] != barrel_sizes[pdb2]:
                    subnetwork.write("\t".join(line) + "\n")
                
                
                