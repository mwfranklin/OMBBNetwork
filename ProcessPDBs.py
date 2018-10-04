import os
import shutil
import glob
import PDBparser as pdbp
import PDBmanip as pdbm
import textwrap

"""for filename in glob.glob("PDBFiles/*.pdb"):
    #print(filename)
    check_lines = False
    with open(filename, "r") as pdb_file:
        for line in pdb_file:
            if "ATOM" == line[0:4] and check_lines == False: 
                #print(line[22:26])
                check_lines = True
        if check_lines == False:
            print(filename)"""

for filename in glob.glob("PDBFiles/*.pdb"):
    pdb_id = filename.split("/")
    pdb_id = pdb_id[-1][:-4]
    #print(pdb_id)
    if pdb_id == "3jc8_Qd" or pdb_id == "4v6m_AZ":
        continue
    with open(filename, "r") as pdb_file:
        pdb_lines = pdb_file.readlines()
    sequence = pdbm.pdb_to_seq(pdb_lines, filename[-5])
    pdb_seq = pdbm.seq_from_struct(pdb_lines, filename[-5])
    #print(sequence)
    #print(pdb_seq)
    if "Soeding" in pdb_lines[1]:
        #print("pdb has been adjusted")
        continue
    else:
        #print("Checking file %s, chain is %s" %(pdb_id, filename[-5]))
        data_seq = ""
        remark_lines = []
        for line in pdb_lines:
            if "REMARK" in line:
                remark_lines.append(line.strip())
        if "This file" in remark_lines[0]:
            remark_lines = remark_lines[3:]
        else:
            remark_lines = remark_lines[1:]
        for entry in remark_lines:
            data_seq += entry[10:]
        sequence = data_seq
        #print(sequence)
        #print(pdb_seq)
        atom_records = pdbm.one_chain_lines(pdb_lines, filename[-5])
        #atom_records = pdb_lines[:]
        if pdb_seq[0:20] == sequence[0:20]:
            #print(pdb_id, "Same seq")
            atom_records, adj_factor = pdbm.renumber_pdb_inplace(atom_records, 1)
        else:
            interupt = sequence.split(pdb_seq[0:20])
            if len(interupt) == 1:
                print(pdb_id)
                print(sequence)
                print("Seq to match: ", pdb_seq)
                new_start = int(input("Please enter the start value:"))
            else:
                new_start = len(interupt[0])+1
            #print(pdb_id, len(interupt[0]))
            atom_records, adj_factor = pdbm.renumber_pdb_inplace(atom_records, new_start)
        if adj_factor != 0:
            print(pdb_id, adj_factor)
            with open("PDBFiles/%s.pdb"%pdb_id, "w+") as pdb_file:
                pdb_file.write("HEADER    PDB chain %s \t Oct 3, 2018\n"%pdb_id)
                pdb_file.write("REMARK    Sequence of PDB:\n")
                sequence = textwrap.wrap(sequence, 50)
                for x in sequence:
                    pdb_file.write("REMARK    %s\n"%x)
                for value in atom_records:
                    pdb_file.write(value)