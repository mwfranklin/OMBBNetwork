import re
import glob
import sys
import numpy as np
import PDBparser as pdbp
import os
import subprocess

def renumber_edges(domain1, sequence1):
    with open("PDBFiles/%s.pdb"%domain1, "r") as pdb_file:
        pdb_lines = pdb_file.readlines()
    start = False
    seq_pdb = ""
    for row in pdb_lines:
        if "REMARK    >" in row or "REMARK    Sequence" in row:
            start = True
        elif "REMARK" in row and start == True:
            seq_pdb += row.strip()[10:]
    #print(seq_pdb)

    old_seq = seq_pdb.split(sequence1) #determine if the entirety of sequence is in the PDB
    if len(old_seq) !=1:
        #renumber all edge data to match 1-indexed positions of PDB
        new_start = len(old_seq[0]) + 1
        new_end = new_start + len(sequence1) - 1
        print(new_start, new_end)
    else: #if not, manually seek the correct position - most often this is due to His tags, Met at beginning, a single missing/extra residue, X instead of name, etc.
        print(dom1)
        print(old_seq)
        print("Seq to match: ", sequence1)
        new_start = int(input("Please enter the start value:"))
        new_end = new_start + len(sequence1) - 1
    
    return new_start, new_end

incorrect_frags = []
with open("DupPDBs_v6.txt", "r") as inData:
    for line in inData:
        incorrect_frags.append(line.strip())

dom_list = []
with open("rawData_E20_v6_2018_test.txt", "r") as edge_list, open("rawData_E20_v6_2018_Renumb.txt", "w+") as new_edges:
    for line in edge_list:
        if "dom1" not in line:
            line = line.strip().split("\t")
            dom1 = line[0]
            dom2 = line[1]
            seq1 = line[11]
            seq2 = line[12]
        
            #remove gaps from sequences
            seq1 = seq1.replace("-", "")
            seq2 = seq2.replace("-", "")
        
            print(dom1, dom2)
            if dom1 in incorrect_frags:
                continue
            if dom2 in incorrect_frags:
                continue
            
            new_start1, new_end1 = renumber_edges(dom1, seq1)
            new_start2, new_end2 = renumber_edges(dom2, seq2)
        
            new_edges.write("\t".join(line[0:7]) + "\t" + str(new_start1) + "\t" + str(new_end1) + "\t" + str(new_start2) + "\t" + str(new_end2) + "\t" + "\t".join(line[11:]) + "\n")