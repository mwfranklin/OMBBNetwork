import pandas
import feather
import numpy as np
import re
import math

seq_IDs = ["85", "50", "25"]
barrels = {}
with open("BarrelChars85.txt", "r") as barrel_data:
  for line in barrel_data:
    if "PDB" not in line:
      line = line.strip().split()
      barrels[line[0]] = int(line[1])
#print(barrels)

#for value in seq_IDs:  
value = "85"
allowed_barrels = []
with open("/Users/meghan/Documents/PhD/SluskyLab/DBList_v4_%s.txt"%value, "r") as allowed_data:
    for line in allowed_data:
        allowed_barrels.append(line.strip().lower())

prototypical = []
with open("CompCodesE<1.txt", "r") as comp_data:
    for line in comp_data:
        line = line.strip().split("\t")
        if line[1] == "1" and line[0][0:4] in allowed_barrels:
            prototypical.append(line[0])

avg_interaction = np.zeros([27,27])
int_counts = np.zeros([27,27])
e_values = [ [ [] for i in range(27)] for j in range(27)]
diff_barrel_lines = [ [ [] for i in range(27)] for j in range(27)]
with open("16_18DataOnly_test.txt", "r") as inData:
    for line in inData:
        if "IntNum" not in line:
            line = line.strip().split()
            if line[1] in prototypical and line[2] in prototypical and float(line[3]) <= 1e-2: #add line[-1] == "1" for min e-value calcs; remove float(line[3]) if not looking at Fig 4 tiers.
                #print(line[1], line[2])
                #print(barrels[line[1]], barrels[line[2]])
                e_values[ barrels[line[1]]][ barrels[line[2]] ].append(float(line[3]))
                e_values[ barrels[line[2]]][ barrels[line[1]] ].append(float(line[3]))
                keep_piece = line[0:4] + line[6:8]
                diff_barrel_lines[ barrels[line[1]]][ barrels[line[2]] ].append(keep_piece)
                diff_barrel_lines[ barrels[line[2]]][ barrels[line[1]] ].append(keep_piece)
                avg_interaction[barrels[line[1]], barrels[line[2]]] += float(line[3])
                avg_interaction[barrels[line[2]], barrels[line[1]]] += float(line[3])
                int_counts[barrels[line[1]], barrels[line[2]]] += 1
                int_counts[barrels[line[2]], barrels[line[1]]] += 1
#print(avg_interaction)
#print(e_values)

for x in range(23):
    for y in range(x+1, 23):
        if len(e_values[x][y]) > 1:
            print(x, y)
            print(min(e_values[x][y]), max(e_values[x][y]))
            for entry in diff_barrel_lines[x][y]:
                entry[4] = re.split(",", entry[4])
                entry[4] = sorted([int(x.split("strand")[-1]) for x in entry[4]])
                entry[5] = re.split(",", entry[5])
                entry[5] = sorted([int(x.split("strand")[-1]) for x in entry[5]])
                #if len(entry[4]) != len(entry[5]):
                 #   print(entry)
shared_8str = []
for entry in diff_barrel_lines[8][16]: 
    if barrels[entry[1]] == 16:
        shared_8str.append(entry[1])
    else:
        shared_8str.append(entry[2])
    #print(entry)
shared_8str = sorted(set(shared_8str))
shared_16str = []
for entry in diff_barrel_lines[16][18]:
    if barrels[entry[1]] == 16:
        shared_16str.append(entry[1])
    else:
        shared_16str.append(entry[2])
    #print(entry)
needed = sorted(set(shared_16str).intersection(shared_8str))
print(needed)
count = 0
for entry in diff_barrel_lines[8][16]:
    if entry[1] not in needed and entry[2] not in needed:
        print(entry)
        count += 1
print(count)
count = 0
for entry in diff_barrel_lines[16][18]:
    if entry[1] in needed or entry[2] in needed:
        print(entry)
        count += 1
print(count)

all_8str = []
for x in range(9):
    for y in range(x+1, 13):
        count = 0
        for entry in diff_barrel_lines[x][y]:                
            print(entry)
            count += 1
            if barrels[entry[1]] == 8:
                all_8str.append(entry[1])
            else:
                all_8str.append(entry[2])
        print(count)
print(sorted(set(all_8str)))
            

used_strands = [np.zeros(x) for x in range(23) ]
for x in range(23):
    for y in range(x+1, 23):
        if len(e_values[x][y]) > 1:
            print(x, y, int_counts[x][y])
            terminal_align = 0
            non_hairpins = []
            terminal_strands = 0
            lengths = np.zeros(x+1)
            used_strands_x = np.zeros(x)
            used_strands_y = np.zeros(y)
            for entry in diff_barrel_lines[x][y]:                
                print(entry)
                """#identify conserved strands across all alignments
                for pos in entry[4]:
                    #print(entry[1], barrels[entry[1]], pos)
                    used_strands[barrels[entry[1]]][pos] += 1
                for pos in entry[5]:
                    #print(entry[2], barrels[entry[2]], pos)
                    used_strands[barrels[entry[2]]][pos] += 1
                #identify conserved strands within this pair of barrel sizes
                if barrels[entry[1]] == x:
                    for pos in entry[4]:
                        #print(entry[1], barrels[entry[1]], pos)
                        used_strands_x[pos] += 1
                    for pos in entry[5]:
                        #print(entry[2], barrels[entry[2]], pos)
                        used_strands_y[pos] += 1
                else:
                    for pos in entry[4]:
                        #print(entry[1], barrels[entry[1]], pos)
                        used_strands_y[pos] += 1
                    for pos in entry[5]:
                        #print(entry[2], barrels[entry[2]], pos)
                        used_strands_x[pos] += 1"""
                #identify any alignments between terminal strands or falling into that pattern
                if abs(entry[4][-1] - entry[5][-1]) == abs(barrels[entry[1]] - barrels[entry[2]]):
                    #print("Terminal Align", entry)
                    terminal_align += 1
                    lengths[len(entry[4])]+=1
                    if barrels[entry[1]] == x:
                        if entry[4][-1] == x-1: terminal_strands += 1
                        #else: print(entry)
                    else:
                        if entry[5][-1] == x-1: terminal_strands += 1
                        #else: print(entry)
                else:
                    non_hairpins.append(entry[0])
                
            print(terminal_align, lengths, terminal_strands, non_hairpins)
            #print(used_strands_x, used_strands_y)

for x in range(23):
    print(x, used_strands[x])

c_term_align = 0
n_term_align = 0
for entry in diff_barrel_lines[16][18]:                
    #identify any alignments between terminal strands or falling into that pattern
    if abs(entry[4][-1] - entry[5][-1]) == 2 and len(entry[4]) == len(entry[5]):
        #print("C-Terminal Align", entry)
        c_term_align += 1
    elif entry[4][0] == entry[5][0] and len(entry[4]) == len(entry[5]):
        #print("N-Terminal Align", entry)
        n_term_align += 1
        """terminal_align += 1
        lengths[len(entry[4])]+=1
        if barrels[entry[1]] == x:
            if entry[4][-1] == x-1: terminal_strands += 1
            #else: print(entry)
        else:
            if entry[5][-1] == x-1: terminal_strands += 1
            #else: print(entry)"""
    else:
        print("Oddball", entry)
        #non_hairpins.append(entry[0])
print(c_term_align, n_term_align)
            
