import re
import glob
import sys

out_file = "BarrelsOnlyE20.txt"
cutoff = 20

protos = []
barrels = []
with open("CompCodesE<1.txt", "r") as barrel_codes:
    for line in barrel_codes:
        line = line.strip().split("\t")
        barrels.append(line[0])
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

needed_barrels = barrels
with open("data/AllDataE20_v6_Numbered.txt", "r") as inData, open("data/%s"%out_file, "w+") as subnetwork:
    for line in inData:
        if "Dom1" in line:
            subnetwork.write(line)
        else:
            line = line.strip().split(" ")
            pdb1 = line[1]
            pdb2 = line[2]
            
            if pdb1 in needed_barrels and pdb2 in needed_barrels and float(line[3]) <= cutoff:
                subnetwork.write(" ".join(line) + "\n")
                
                
                