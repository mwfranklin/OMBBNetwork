import os
import sys
import glob
import re
import subprocess

for filename in glob.glob("MSAs/*.a3m"):
    pdb_id = filename.split("/")[-1][:-4]
    os.system("hhalign -i %s -o data/IntRepeats/%s_Score.txt"%(filename, pdb_id))
 
barrels = []
with open("BarrelChars85.txt", "r") as barrel_list:
    for line in barrel_list:
        if "PDB" not in line:
            barrels.append(line.split()[0].upper())

with open("data/CollatedIntRpts.txt", "w+") as outdata:
    outdata.write("PDB\t\tProb E-value P-value  Score    SS Cols Query HMM  Template HMM\tQuery Strands\tTemplate Strands\n")
    
    for filename in glob.glob("data/IntRepeats/*_Score.txt"):
        kept_lines = []
        pdb_ID = filename.split("/")[-1][:-10]
        print(pdb_ID)
        if pdb_ID in barrels:  
            with open(filename, "r") as score_file:
                keep_line = False
                for line in score_file:
                    if "No Hit" in line:
                        keep_line = True
                    if "No 1" in line:
                        keep_line = False
    
                    if keep_line == True:
                        kept_lines.append(line)
            if len(kept_lines) > 0: print(pdb_ID) 
            for value in kept_lines[1:-1]:
                value = value[36:].strip().split()
                print(value)
                if (float(value[0]) < 75 or float(value[1]) > 1E-2): continue
                else:
                    query = value[6].split("-")
                    query = [int(x) for x in query]
                    template = value[7].split("(")[0].split("-")
                    template = [int(x) for x in template]
                    print(query, template)
                    #something about strands...                
                    query_strands = []
                    template_strands = []
                    with open("InOut/InOut_%s.txt"%pdb_ID[0:4].upper(), "r") as strands:
                        for line in strands:
                            if "Res" not in line:
                                line = line.split("\t")
                                if (int(line[1]) in range(query[0], query[1]+1) and line[3] == pdb_ID[-1]): query_strands.append(int(line[2]))
                                if (int(line[1]) in range(template[0], template[1]+1) and line[3] == pdb_ID[-1]): template_strands.append(int(line[2]))
                    #print(sorted(set(template_strands)), sorted(set(query_strands)))
                    template_strands = sorted(set(template_strands))
                    query_strands = sorted(set(query_strands))                              
                                                
                    outdata.write("%s\t%s\t%s\t%s\n"%(pdb_ID, "\t".join(value[2:]), ",".join(map(str, query_strands)), ",".join(map(str, template_strands))))