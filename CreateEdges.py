import re
import glob
import sys
import numpy as np
from collections import Counter

def get_strands(pdb_id, aligned_res):
    #only strands with 3+ res get added to list of aligned strands
    strands1 = {}
    try:
        with open("InOut/InOut_%s.txt"%pdb_id[0:4].upper(), "r") as pdb1_strands:
            for row in pdb1_strands:
                if "Res" not in row:
                    row = row.split("\t")
                    if row[3].strip() == pdb_id[-1]:
                        strands1[row[1]] = int(row[2])
        #print(strands1)
        strand_res1 = []
        for key in strands1:
            if int(key) in aligned_res:
                #res1[res1.index(key)] = strands1[key]
                strand_res1.append(strands1[key])
        strand_lengths1 = Counter(strand_res1)
        for entry in Counter(strand_res1).keys():
            if Counter(strand_res1)[entry] <= 2:
                del strand_lengths1[entry]
        strand_res1 = sorted(set(strand_lengths1.keys()))
        strand_res1 = ["strand"+str(x) for x in strand_res1]
                                
    except FileNotFoundError:
        #print("Can't find file", pdb1)
        strand_res1 = res1
    
    #print(strand_res1)        
    return strand_res1

def pymol_ranges(resnums):
    ranges1 = []
    start_pt = resnums[0]
    k = 1
    conseqcount = 1
    while k<len(resnums)-1:
        if resnums[k] == start_pt + conseqcount:
            conseqcount +=1
        else:
            if start_pt == resnums[k-1]:
                ranges1.append(str(start_pt))
            else:
                ranges1.append("%s-%s"%(start_pt, resnums[k-1]))
            start_pt = resnums[k]
            conseqcount = 1
        k+=1
    #print(start_pt, conseqcount, strand_res1)
    if conseqcount != 1:
        ranges1.append("%s-%s"%(start_pt, resnums[k]))
    else:
        #print(start_pt +conseqcount, "Wrong number", res1[k])
        ranges1.append(str(start_pt))
    #print(strand_res1)
    return ranges1

in_file = "AllDataE1_v6.txt"
out_file = "AllDataE1_v6_Numbered.txt"

barrel_sizes = {}
all_barrels = []
with open("BarrelChars85.txt", "r") as barrel_list:
    for line in barrel_list:
        if "Barrel" not in line:
            line = line.split("\t")
            all_barrels.append(line[0])
            barrel_sizes[line[0]] = int(line[1])
incorrect_frags = []
with open("DupPDBs_v6.txt", "r") as inData:
    for line in inData:
        incorrect_frags.append(line.strip())

dom_list = []
count = 1
with open("data/%s"%in_file, "r") as inData, open("data/%s"%out_file, "w+") as outdata, open("data/%s_Tab.txt"%out_file[:-4], "w+") as tabbed_out:    
    #outdata.write("interaction Dom1 Dom2 E-value Res1 Res2 Strand1 Strand2 Seq1 Seq2 HHS_Prob HHS_Score Length Perc_ID Perc_Sim RMSD TMScore MaxSub GDT_TS GDT_HA InCyto?\n")
    for line in inData:
        if "dom1" in line:
            outdata.write("interaction Dom1 Dom2 E-value Res1 Res2 Strand1 Strand2 Seq1 Seq2 HHS_Prob HHS_Score Length Perc_ID Perc_Sim RMSD TMScore MaxSub GDT_TS GDT_HA InCyto?\n")
            tabbed_out.write("interaction\tDom1\tDom2\tE-value\tRes1\tRes2\tStrand1\tStrand2\tSeq1\tSeq2\tHHS_Prob\tHHS_Score\tLength\tPerc_ID\tPerc_Sim\tRMSD\tTMScore\tMaxSub\tGDT_TS\tGDT_HA\tInCyto?\n")
        else:    
            line = line.strip().split("\t")
            if line[14] == "ERR":
                continue
            #print(line)
            dom1 = line[0]
            dom2 = line[1]
            e_value = line[2]
            start1 = int(line[6])
            start2 = int(line[8])
            seq1 = line[10]
            seq2 = line[11]
            res1 = []
            res2 = []
            
            if dom1 in incorrect_frags:
                continue
            if dom2 in incorrect_frags:
                continue
                
            dom_list.append(dom1)
            dom_list.append(dom2)    
            #print(seq1)
            #print(len(seq1), len(seq2), len(res1), len(res2))
            
            count1 = 0
            count2 = 0
            for x in range(0, len(seq1)):
                if seq1[x] == "-": 
                    #print("GAP", seq1[x], seq2[x], count2 + start2)
                    count2 += 1
                elif seq2[x] == "-":
                    #print("GAP", seq1[x], seq2[x], count1 + start1)
                    count1 += 1
                else:
                    res1.append(start1 + count1)
                    res2.append(start2 + count2)
                    count1 +=1
                    count2 +=1

            #print(res1)
            #print(res2)
            
            pymol_range1 = pymol_ranges(res1)
            pymol_range2 = pymol_ranges(res2)
            strands1 = get_strands(dom1, res1)
            strands2 = get_strands(dom2, res2)
            
            outdata.write("%s %s %s %s %s %s %s %s %s %s %s\n" %(count, dom1, dom2, e_value, ",".join(map(str, pymol_range1)), ",".join(map(str, pymol_range2)), ",".join(map(str, strands1)), ",".join(map(str, strands2)), " ".join(line[10:14]), " ".join(line[3:6]), " ".join(line[14:]) ))
            tabbed_out.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %(count, dom1, dom2, e_value, ",".join(map(str, pymol_range1)), ",".join(map(str, pymol_range2)), ",".join(map(str, strands1)), ",".join(map(str, strands2)), "\t".join(line[10:14]), "\t".join(line[3:6]), "\t".join(line[14:]) ))
        
            count +=1
print(count)
print(set(all_barrels).difference(set(dom_list)))    