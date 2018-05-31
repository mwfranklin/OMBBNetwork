import os
import numpy as np
import glob

aa = ["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL", "MSE", "SEC"]
oneletAA = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V", "M", "C"]

def fix_InOut_files(first_strand_seq, barrel_start, pdb_name, chain):
    data_seq = ""
    remark_lines = []
    with open("PDBFiles/%s_%s.pdb"%(pdb_name, chain), "r") as inData:
        for line in inData:
            if "REMARK" in line:
                remark_lines.append(line.strip())
    if "This file" in remark_lines[0]:
        remark_lines = remark_lines[3:]
    else:
        remark_lines = remark_lines[1:]
    for entry in remark_lines:
        data_seq += entry[10:]
    #print(data_seq)
    data_seq = data_seq.split(first_strand_seq)
    if len(data_seq) != 2:
        print("Big problems")
    else:
        new_start = len(data_seq[0]) + 1
        if new_start != barrel_start:
            diff = new_start - barrel_start
            print(barrel_start, new_start, diff, data_seq[0])
            with open("InOut/InOut_%s.txt"%pdb_name.upper(), "r") as inData, open("InOut/Mod_InOut_%s.txt"%pdb_name.upper(), "w+") as outData:
                for line in inData:
                    if "Res" in line:
                        outData.write(line)
                    else:
                        line = line.split("\t")
                        line[1] = str(int(line[1]) + diff)
                        outData.write("\t".join(line))
            

chains = {}
with open("BarrelChars85.txt", "r") as inData:
    for line in inData:
        line = line.split("\t")
        chains[line[0][0:4]] = line[0][-1]
    
for filename in glob.glob("InOut/InOut_*.txt"):
    pdb_id = filename.split("/")[-1][6:-4].lower()
    print(pdb_id)
    if pdb_id == '3b07' or pdb_id == "4tw1":
        continue
    first_strand = ""
    first_strand_res = 999    
    with open(filename, "r") as inData:
        for line in inData:
            if "Res" not in line:
                line = line.strip().split("\t")
                line[0] = oneletAA[aa.index(line[0])]
                if line[2] == "0" and line[3] == chains[pdb_id]:
                    first_strand += line[0]
                    if int(line[1]) < first_strand_res:
                        first_strand_res = int(line[1])
    
    fix_InOut_files(first_strand, first_strand_res, pdb_id, chains[pdb_id])