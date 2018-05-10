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
        print(strands1)
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
    
    print(strand_res1)        
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

in_file = "16_18DataOnly.txt"
out_file = "16_18DataOnly_test.txt"

barrel_sizes = {}
all_barrels = []
with open("BarrelChars85.txt", "r") as barrel_list:
    for line in barrel_list:
        if "Barrel" not in line:
            line = line.split("\t")
            all_barrels.append(line[0])
            barrel_sizes[line[0]] = int(line[1])

dom_list = []
count = 1
cutoff = 1
with open(in_file, "r") as inData, open(out_file, "w+") as outdata:    
    outdata.write("interaction Dom1 Dom2 E-value Res1 Res2 Strand1 Strand2 Seq1 Seq2 HHS_Prob HHS_Score Length Perc_ID Perc_Sim RMSD TMScore MaxSub GDT_TS GDT_HA InCyto?\n")
    for line in inData:
        if "dom1" in line:
            outdata.write("interaction Dom1 Dom2 E-value Res1 Res2 Strand1 Strand2 Seq1 Seq2 HHS_Prob HHS_Score Length Perc_ID Perc_Sim RMSD TMScore MaxSub GDT_TS GDT_HA InCyto?\n")
        else:    
            line = line.strip().split("\t")
            #print(line)
            dom1 = line[0]
            dom2 = line[1]
            e_value = line[2]
            start1 = int(line[7])
            start2 = int(line[9])
            seq1 = line[11]
            seq2 = line[12]
            #line[15] = line[3]
            #line[16] = line[4]
            #print(start1, end1)
            res1 = []
            res2 = []
        
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
            
            #outdata.write("%s %s %s %s %s %s %s %s %s\n" %(count, dom1, dom2, e_value, ",".join(map(str, pymol_range1)), ",".join(map(str, pymol_range2)), ",".join(map(str, strands1)), ",".join(map(str, strands2)), " ".join(line[11:]) ))
            outdata.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %(count, dom1, dom2, e_value, ",".join(map(str, pymol_range1)), ",".join(map(str, pymol_range2)), ",".join(map(str, strands1)), ",".join(map(str, strands2)), "\t".join(line[7:]) ))
        
            count +=1

"""with open("v4_July/NumberedEdgesE<1July.txt", "r") as inData:    
    inData = inData.readlines()
    
with open("v4_July/NumberedEdgesE<1July_Fix.txt", "w+") as outData:
    for line in inData:
        line = line.split("\t")
        if len(line)>2:
            if line[11] == "ERR":
                outData.write("\t".join(line[:12])+ "\tERR"*4 + "\t" + line[-1])
            else:
                outData.write("\t".join(line))
        else:
            outData.write("\t".join(line))"""