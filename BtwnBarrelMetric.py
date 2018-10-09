import pandas
import feather
import numpy as np
import re
import math
import textwrap
import matplotlib.pyplot as plt
from collections import Counter

def write_btwnbarrels_feather(e_values, seq_id):
    e_values_1 = np.zeros([27,27])
    e_values_3 = np.zeros([27,27])
    e_values_5 = np.zeros([27,27])
    #print(e_values)
    for x in range(0,len(e_values)):
        for y in range(0,len(e_values[x])):
            #print(x, y)
            e_values_1[x,y] = sum([1 for item in e_values[x][y] if item <= 0.001])
            e_values_3[x,y] = sum([1 for item in e_values[x][y] if item <= 0.00001])
            e_values_5[x,y] = sum([1 for item in e_values[x][y] if item <= 0.0000001])
    
    e_values_1 = pandas.DataFrame(e_values_1)
    feather.write_dataframe(e_values_1.copy(), "data/BtwnBarrels/BtwnBarrelEVals3_%s.feather"%seq_id)
    e_values_3 = pandas.DataFrame(e_values_3)
    feather.write_dataframe(e_values_3.copy(), "data/BtwnBarrels/BtwnBarrelEVals5_%s.feather"%seq_id)
    e_values_5 = pandas.DataFrame(e_values_5)
    feather.write_dataframe(e_values_5.copy(), "data/BtwnBarrels/BtwnBarrelEVals7_%s.feather"%seq_id)

def write_conslengths_feather(strand_lengths, strand_ids, seq_id):
    strand_ids = [Counter(x) for x in strand_ids]
    for x in range(0,23):
        if len(strand_ids[x]) == 0:
            strand_ids[x] = 0
        else:
            temp_size = []
            for y in range(0,x): 
                try:
                    temp_size.append(strand_ids[x][y])
                except:
                    temp_size.append(0)
            strand_ids[x] = temp_size
    
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
    #print(strand_lengths)
    
    barrel_sizes = [8, 10, 12, 14, 16, 18, 22]
    export_lengths = np.zeros([7,22])
    export_IDs = np.zeros([7,22])
    for value in range(0,len(barrel_sizes)):
        for x in range(0,barrel_sizes[value]):
            export_lengths[value][x] = strand_lengths[barrel_sizes[value]][x]
            export_IDs[value][x] = strand_ids[barrel_sizes[value]][x]
    print(export_IDs)
    #print(export_lengths)
    export_IDs = pandas.DataFrame(export_IDs)
    feather.write_dataframe(export_IDs.copy(), "data/ConsStrandIDs%s.feather"%seq_id)
    export_lengths = pandas.DataFrame(export_lengths)
    feather.write_dataframe(export_lengths.copy(), "data/ConsLengths%s.feather"%seq_id)

def graph_hist_of_pairs_of_lengths(lengths_by_lengths, graph_hist, labels, seq_id):
    total_lengths = [ [len(x) for x in y] for y in lengths_by_lengths]
    lengths_by_lengths = [ [Counter(x) for x in y] for y in lengths_by_lengths]
    for x in range(0,23):
        for y in range(0,23):
            if len(lengths_by_lengths[x][y]) == 0:
                lengths_by_lengths[x][y] = 0
            else:
                temp_size = []
                #print(lengths_by_lengths[x][y])
                for z in range(1,y+1): 
                    try:
                        temp_size.append(lengths_by_lengths[x][y][z])
                    except:
                        temp_size.append(0)
                lengths_by_lengths[x][y] = temp_size
            
    fig, axes = plt.subplots(nrows = 3, ncols = 3, figsize = (16, 16))
    axes = axes.flatten()
    for value in range(0, len(graph_hist)):
        ind = np.arange(1,graph_hist[value][1]+1,1)
        width = 0.5
        ticks = np.arange(2,graph_hist[value][1]+1, 2)
        axes[value].set_xticks(ticks)
        tick_labels = [str(x) for x in ticks]
        axes[value].tick_params(labelsize=18)
        axes[value].set_xticklabels(tick_labels)
        axes[value].annotate(labels[value], xy = (0.03,.91), xycoords = "axes fraction", size = 28)
        axes[value].bar(ind, lengths_by_lengths[graph_hist[value][0]][graph_hist[value][1]], color = "black")
        axes[value].set_xlim([0.75,graph_hist[value][1]+1])
        #ax1.legend(loc = 2, scatterpoints = 1, fontsize = 12)
        title = textwrap.wrap("%s- to %s-stranded Barrels (n = %s)"%(graph_hist[value][0], graph_hist[value][1], total_lengths[graph_hist[value][0]][graph_hist[value][1]]), 40)
        axes[value].set_title("\n".join(title), size=18)
        plt.savefig("NetworkGraphs/TieredHistConservedSizes_%sID_E-3.png"%seq_id)
    plt.tight_layout(w_pad = 1, h_pad = 2)
    plt.subplots_adjust(top=0.91, bottom = 0.08, left = 0.06)
    fig.text(0.5, 0.02, "Number of Strands in Conserved Segment", ha = "center", size = 24)
    fig.text(0.01, 0.5, "Occurence", va = "center", rotation = "vertical", size = 24)
    fig.suptitle(r"Length of Conserved Segments (E-value $\leq 10^{-5})$", size = 32)
    plt.savefig("NetworkGraphs/TieredHistConservedSizes_%sID.png"%seq_id)
    #plt.show()

seq_IDs = ["50", "85", "25"]
barrels = {}
with open("BarrelChars85.txt", "r") as barrel_data:
  for line in barrel_data:
    if "PDB" not in line:
      line = line.strip().split()
      barrels[line[0]] = int(line[1])
#print(barrels)

seq_IDs = ["85"]
for value in seq_IDs:  
    #value = "85"
    #print(value)
    allowed_barrels = []
    with open("/Users/meghan/Documents/PhD/SluskyLab/DBList_v5_%s.txt"%value, "r") as allowed_data:
        for line in allowed_data:
            allowed_barrels.append(line.strip().lower())
    #print(len(allowed_barrels))
    
    prototypical = []
    counts = np.zeros(27)
    with open("CompCodesE-3.txt", "r") as comp_data:
        for line in comp_data:
            line = line.strip().split("\t")
            if line[1] == "1" and line[0][0:4] in allowed_barrels:
                prototypical.append(line[0])
                counts[barrels[ line[0] ]] += 1
    #print(len(prototypical))
    #with open("data/BtwnBarrels/ProtoLengths.txt", "a") as outData:
     #   outData.write(value + "%\t" + "\t".join(map(str, counts)) + "\n")
    
    avg_interaction = np.zeros([27,27])
    int_counts = np.zeros([27,27])
    e_values = [ [ [] for i in range(27)] for j in range(27)]
    diff_barrel_lines = [ [ [] for i in range(27)] for j in range(27)]
    with open("data/AllDataE1_v6_Numbered.txt", "r") as inData:
        for line in inData:
            if "IntNum" not in line:
                line = line.strip().split()
                if line[1] in prototypical and line[2] in prototypical and float(line[3]) <= 1e-3:# and line[-1] == "1": #add line[-1] == "1" for min e-value calcs; change float(line[3]) to 1e-5 for tree diagram
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
    
    avg_interaction /= int_counts
    test_e_values = np.zeros([27,27])
    for x in range(27):
        for y in range(27):
            test_e_values[x][y] = np.exp(np.mean(np.log(e_values[x][y])))
            
    """write_btwnbarrels_feather(e_values, value)
    avg_interaction = pandas.DataFrame(avg_interaction)
    test_e_values = pandas.DataFrame(test_e_values)
    feather.write_dataframe(avg_interaction.copy(), "data/BtwnBarrels/BtwnBarrelMetric_%s.feather"%value)
    feather.write_dataframe(test_e_values.copy(), "data/BtwnBarrels/BtwnBarrelMetricLog_%s.feather"%value)"""
    
    strand_lengths = [[] for x in range(0,23)]
    strand_IDs = [[] for x in range(0,23)]
    lengths_by_lengths = [ [ [] for i in range(23)] for j in range(23)]
    for x in range(8,23):
        for y in range(x, 23):
            if len(e_values[x][y]) > 1:
                #print(x, y)
                #print(e_values[x][y])
                #print(min(e_values[x][y]), max(e_values[x][y]), test_e_values[x][y], avg_interaction[x][y])
                diff_barrel_lines[x][y] = [list(i) for i in set(tuple(i) for i in diff_barrel_lines[x][y])]
                for entry in diff_barrel_lines[x][y]:
                    #print(entry)
                    entry[4] = re.split(",", entry[4])
                    entry[5] = re.split(",", entry[5])
                    if len(entry[4]) > 1:
                        entry[4] = sorted([int(x.split("strand")[-1]) for x in entry[4]])
                    else: entry[4] = []
                    if len(entry[5]) > 1:
                        entry[5] = sorted([int(x.split("strand")[-1]) for x in entry[5]])
                    else: entry[5] = []
                    
                    strand_lengths[barrels[entry[1]]].append(len(entry[4]))
                    strand_lengths[barrels[entry[2]]].append(len(entry[5]))
                    lengths_by_lengths[barrels[entry[1]]][ barrels[entry[2]] ].append(len(entry[4]))
                    lengths_by_lengths[barrels[entry[2]]][ barrels[entry[1]] ].append(len(entry[5]))
                    
                    for strand in entry[4]:
                        strand_IDs[barrels[entry[1]]].append(strand)
                    for strand in entry[5]:
                        strand_IDs[barrels[entry[2]]].append(strand)
                    #if len(entry[4]) != len(entry[5]):
                     #   print(entry)
    #print(strand_IDs)
    
    #write_conslengths_feather(strand_lengths, strand_IDs, value)
    #if value == "85":
     #   graph_hist_of_pairs_of_lengths(lengths_by_lengths, [ [8, 10], [8, 12], [8,14], [8,16], [10, 12], [12,14], [12, 16], [14,22], [16,18]  ], ["A", "B", "C", "D", "E", "F", "G", "H", "J"] , value)
    
used_strands = [np.zeros(x) for x in range(27) ]
for x in range(8,23):
    for y in range(x+1, 23):
        if len(e_values[x][y]) > 1:
            print(x, y, "total aligns:",int_counts[x][y])
            c_terminal_align = 0
            n_terminal_align = 0
            double_hairpin = 0
            non_hairpins = []
            terminal_strands = 0
            lengths = np.zeros(x+1)
            used_strands_x = np.zeros(x)
            used_strands_y = np.zeros(y)
            for entry in diff_barrel_lines[x][y]:                
                #print(entry)
                #identify conserved strands across all alignments
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
                        used_strands_x[pos] += 1
                #identify any alignments between c-terminal strands or falling into that pattern
                if len(entry[4]) != len(entry[5]):
                    print("diff lengths", entry)
                    non_hairpins.append(entry[0])
                elif abs(entry[4][-1] - entry[5][-1]) == abs(barrels[entry[1]] - barrels[entry[2]]):
                    #print("Terminal Align", entry)
                    c_terminal_align += 1
                    lengths[len(entry[4])]+=1
                    if barrels[entry[1]] == x:
                        if entry[4][-1] == x-1: terminal_strands += 1
                        #else: print(entry)
                    else:
                        if entry[5][-1] == x-1: terminal_strands += 1
                        #else: print(entry)
                elif entry[4][0] == entry[5][0]:
                    #print("N-Terminal Align", entry)
                    n_terminal_align += 1
                elif abs(entry[4][-1] - entry[5][-1]) == 4:
                    print("Double-hairpin Align", entry)
                    double_hairpin += 1
                else:
                    print("nonhairpin", entry)
                    non_hairpins.append(entry[0])
                
            print(c_terminal_align, lengths, terminal_strands)
            print(n_terminal_align, double_hairpin, len(non_hairpins))
            print(used_strands_x, used_strands_y)

for x in range(27):
    print(x, used_strands[x])

c_term_align = 0
n_term_align = 0
double_hairpin = 0
c_term_lengths = np.zeros(17)
n_term_lengths = np.zeros(17)
non_hairpins = []
for entry in diff_barrel_lines[16][18]:                
    #identify any alignments between terminal strands or falling into that pattern
    if abs(entry[4][-1] - entry[5][-1]) == abs(barrels[entry[1]] - barrels[entry[2]]) and len(entry[4]) == len(entry[5]):
        #print("C-Terminal Align", entry)
        c_term_align += 1
        c_term_lengths[len(entry[4])] += 1
    elif entry[4][0] == entry[5][0] and len(entry[4]) == len(entry[5]):
        #print("N-Terminal Align", entry)
        n_term_align += 1
        n_term_lengths[len(entry[4])] += 1
        #start here with quotes: terminal_align += 1
        lengths[len(entry[4])]+=1
        if barrels[entry[1]] == x:
            if entry[4][-1] == x-1: terminal_strands += 1
            #else: print(entry)
        else:
            if entry[5][-1] == x-1: terminal_strands += 1
            #else: print(entry) #end with three quotes
    elif abs(entry[4][-1] - entry[5][-1]) == 4 and len(entry[4]) == len(entry[5]):
        print("Double-hairpin Align", entry)
        double_hairpin += 1
    else:
        print("Oddball", entry)
        non_hairpins.append(entry[0])
print(c_term_align, c_term_lengths, n_term_align, n_term_lengths, double_hairpin)
print(sorted(non_hairpins))          
