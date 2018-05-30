import os
import math
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import stats
import numpy as np
import textwrap


barrels = {}
with open("BarrelChars85.txt", "r") as inData:
    for line in inData:
        if "PDB" not in line:
            line = line.split("\t")
            barrels[line[0]] = int(line[1])

proto_barrels = []
proto_sizes = np.zeros(27)
with open("CompCodesE-2.txt", "r") as inData:
    for line in inData:
        if "PDB" not in line:
            line = line.strip().split("\t")
            #print(line)
            if line[1] == "1": 
                proto_barrels.append(line[0])
                proto_sizes[barrels[line[0]]] += 1
#print(len(proto_barrels))

proto_cons_barrels = []
cons_barrels = np.zeros(27)
strand_cons_patt = np.zeros([27,5]) #columns are for no first strand, no last strand, neither first or last, total repeats, no repeats
with open("data/CollatedIntRpts.txt", "r") as inData:
    for line in inData:
        if "PDB" not in line:
            line = line.strip().split("\t")
            if line[1] in proto_barrels:
                if float(line[3]) <= 1e-3:
                    print(line, len(line))
                    proto_cons_barrels.append(line[1])
                    strand_cons_patt[ barrels[line[1]] ][3] += 1
                    if len(line) == 11:
                        strands = sorted(set([int(x) for x in line[10].split(",")] + [int(x) for x in line[11].split(",")]))
                        #print(strands)
                        if strands[0] != 0:
                            if strands[-1] != barrels[line[0]] - 1:
                                strand_cons_patt[ barrels[line[1]] ] [2] += 1
                            else:
                                strand_cons_patt[ barrels[line[1]] ][0] += 1
                        else:
                            if strands[-1] != barrels[line[1]] - 1:
                                strand_cons_patt[ barrels[line[1]] ][1] += 1
                    else:
                        strand_cons_patt[ barrels[line[1]] ] [2] += 1
                    
                cons_barrels[barrels[line[1]]] += 1
                #if barrels[line[0]] == 18: print(line)

for pdb in set(proto_barrels).difference(proto_cons_barrels):
    strand_cons_patt[ barrels[pdb] ][4] += 1

print(strand_cons_patt)
with open("data/CollatedIntRptsPatterns.txt", "w+") as outData:
    outData.write("NoFirst\tNoLast\tNeitherFL\tTotalRpts\tNoRpts\n")
    for line in strand_cons_patt:
        outData.write("\t".join(map(str, line)) + "\n")
        
#print(proto_sizes)
#print(cons_barrels, sum(cons_barrels))
print(sorted(proto_cons_barrels))

ind = np.arange(0,27)
fig, ax1 = plt.subplots(nrows = 1, ncols = 1, figsize = (9,6))
#plt.title("Internal Repeats of the Prototypical Barrels", size = 22)
ax1.set_xlabel("Total Strands per Barrel", size = 46)
ax1.set_ylabel(r"Count", size = 46)
width = 0.5
ax1.bar(ind, proto_sizes, label = "Total Number of Barrels")
ax1.bar(ind, cons_barrels, color = "red", label = "Barrels with Internal Repeat")
ax1.set_xlim([7,23])
ax1.set_xticks(np.arange(8,23,2))
ax1.set_xticklabels(np.arange(8,23,2))
ax1.legend(loc = 0, scatterpoints = 1, fontsize = 18)
#ax1.set_ylim([0,20])
plt.tick_params(labelsize = 26)
plt.tight_layout()
#fig.subplots_adjust(wspace = 0.15)
plt.savefig("NetworkGraphs/ConsProportion_1e3.png", dpi = 300, bbox_inches = "tight")
plt.show()

