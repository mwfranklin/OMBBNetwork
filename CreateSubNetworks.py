import re
import glob
import sys

protos = []
barrels = []
with open("CompCodesE-3.txt", "r") as barrel_codes:
    for line in barrel_codes:
        line = line.strip().split("\t")
        barrels.append(line[0])
        if line[1] == "1":
            protos.append(line[0])

barrel_sizes = [[] for x in range(27)]
with open("BarrelChars85.txt", "r") as barrel_data:
    for line in barrel_data:
        if "PDB" not in line:
            line = line.split("\t")
            if line[0] in protos:
                barrel_sizes[ int(line[1]) ].append(line[0])

count = 0
with open("data/AllDataE1_v6_Numbered.txt", "r") as inData, open("data/ProtosOnlyE-3_v6_Numbered.txt", "w+") as outData:
    for line in inData:
        if "Dom1" in line:
            outData.write(line)
        else:
            line = line.split(" ")
            pdb1 = line[1]
            pdb2 = line[2]
            
            if pdb1 in protos:
                outData.write(" ".join(line))
                count += 1
            elif pdb2 in protos:
                outData.write(" ".join(line))
                count += 1
            else:
                continue
print(count)

cutoff1 = 1e-2
cutoff2 = 1e-3
for x in range(16, 17):
    for y in range(x+1, 19):
        print(x, y)
        keep_lines = []
        with open("data/AllDataE1_v6_Numbered.txt", "r") as inData:
            for line in inData:
                if "Dom1" in line:
                    keep_lines.append(line.strip().split(" "))
                else:
                    line = line.strip().split(" ")
                    pdb1 = line[1]
                    pdb2 = line[2]
                    
                    if float(line[3]) <= cutoff1 and float(line[3]) >= cutoff2:
                        if pdb1 in barrel_sizes[x] and pdb2 in barrel_sizes[y]:
                            keep_lines.append(line)
                        elif pdb1 in barrel_sizes[y] and pdb2 in barrel_sizes[x]:
                            keep_lines.append(line)
                        else:
                            continue
        if len(keep_lines) > 1:
            print(x, y)
            with open("data/BySize/%s_%s_E-3_test.txt"%(x, y), "w+") as subnetwork:
                for value in keep_lines:
                    subnetwork.write("\t".join(value) + "\n")

"""cutoff = 1e-3
count = 0
with open("data/AllDataE20_v6_Numbered.txt", "r") as inData:
    for line in inData:
        if "Dom1" in line:
            keep_lines.append(line.strip().split(" "))
        else:
            line = line.strip().split(" ")
            pdb1 = line[1]
            pdb2 = line[2]
            
            if pdb1 in protos and pdb2 in protos and float(line[3]) <= cutoff and float(line[10]) >= 75:
                count += 1
print(count)
"""
