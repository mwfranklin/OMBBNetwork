#!/usr/bin/env python
import os
import sys
import re
import glob
import math
import matplotlib.pyplot as plt
import numpy as np
import textwrap
from collections import Counter
import pandas
import feather

#in file = 85%, first col is 50%, second col is 25%
seqID_barrels = []
with open("v4_July/DBList_v4_All.txt", "r") as barrel_data:
    for line in barrel_data:
        if "PDB" not in line:
            line = line.strip().split("\t")
            seqID_barrels.append(line[0])
            #if line[1] == "1":
             #   seqID_barrels.append(line[0])

#generate prot0typical list for the hist
prototypical_barrels = []
with open("v4_July/CompCodesE<1.txt", "r") as inData:
    for line in inData:
        line = line.strip().split("\t")
        #rint(line)
        if line[1] == "1" and line[0] in seqID_barrels: prototypical_barrels.append(line[0])
#print(len(prototypical_barrels))

#get lengths associated with 
barrel_sizes = {}
with open("v4_July/BarrelLengths.txt", "r") as inData:
    for line in inData:
        if "PDB" not in line:
            line = line.strip().split("\t")
            if line[0] in prototypical_barrels: barrel_sizes[line[0]] = int(line[1])
#print(barrel_sizes)
    
strand_lengths = [[] for x in range(0,23)]
strand_IDs = [[] for x in range(0,23)]
lengths_by_lengths = [[ [] for x in range(0,23) ] for x in range(0,23)]

with open("v4_July/NumberedEdgesE<1JulyStrands.txt", "r") as cons_data:
    for line in cons_data:
        if "IntNum" not in line:
            line = line.strip().split("\t")
            if (line[1] in prototypical_barrels and line[2] in prototypical_barrels and float(line[3]) <= 0.01):
                strands1 = line[4].split(",")
                strands2 = line[5].split(",")
                #print(strands1, strands2)
                strand_lengths[barrel_sizes[line[1]]].append(len(strands1))
                strand_lengths[barrel_sizes[line[2]]].append(len(strands2))
                for value in strands1:
                    #print(value)
                    if "strand" in value: strand_IDs[barrel_sizes[line[1]]].append(value)
                for value in strands2:
                    if "strand" in value: strand_IDs[barrel_sizes[line[2]]].append(value)
                lengths_by_lengths[ barrel_sizes[line[1]] ][ barrel_sizes[line[2]] ].append(len(strands1))
                lengths_by_lengths[ barrel_sizes[line[2]] ][ barrel_sizes[line[1]] ].append(len(strands2))

strand_lengths = [Counter(x) for x in strand_lengths]
for x in range(0,23):
    if len(strand_lengths[x]) == 0:
        strand_lengths[x] = 0
    else:
        temp_size = []
        for y in range(1,x+1): 
            try:
                temp_size.append(strand_lengths[x][y])
            except:
                temp_size.append(0)
        strand_lengths[x] = temp_size
#print(strand_lengths)"""

barrel_sizes = [8, 10, 12, 14, 16, 18, 22]
export_lengths = np.zeros([7,22])
export_IDs = np.zeros([7,22])
for value in range(0,len(barrel_sizes)):
    #print(value)
    for x in range(0,barrel_sizes[value]):
        #print(strand_lengths[barrel_sizes[value]])
        export_lengths[value][x] = strand_lengths[barrel_sizes[value]][x]
        export_IDs[value][x] = strand_IDs[barrel_sizes[value]][x]
print(export_IDs)
print(export_lengths)
export_IDs = pandas.DataFrame(export_IDs)
feather.write_dataframe(export_IDs.copy(), "/Users/meghan/Dropbox (Slusky Lab)/MFranklin/Publications/strand_evolution_manuscript/repeat protein/Figures/ConsStrandIDs85.feather")
export_lengths = pandas.DataFrame(export_lengths)
feather.write_dataframe(export_lengths.copy(), "/Users/meghan/Dropbox (Slusky Lab)/MFranklin/Publications/strand_evolution_manuscript/repeat protein/Supplement/ConsLengths85.feather")
