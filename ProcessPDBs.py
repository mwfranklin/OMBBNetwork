import os
import shutil
import glob
import PDBparser as pdbp
import textwrap

for filename in glob.glob("PDBFiles/*.pdb"):
    #print(filename)
    check_lines = False
    with open(filename, "r") as pdb_file:
        for line in pdb_file:
            if "ATOM" == line[0:4] and check_lines == False: 
                #print(line[22:26])
                check_lines = True
        if check_lines == False:
            print(filename)

for filename in glob.glob("PDBFiles/*.pdb"):
    pdb_id = filename.split("/")
    pdb_id = pdb_id[-1][:-4]
    print(pdb_id)
    if pdb_id == "3jc8_Qd" or pdb_id == "4v6m_AZ":
        continue
    
    with open(filename, "r") as pdb_file:
        pdb_lines = pdb_file.readlines()
    sequence = pdbp.pdb_to_seq(pdb_lines, filename[-5])
    pdb_seq = pdbp.seq_from_struct(pdb_lines, filename[-5])
    #print(sequence)
    if "PDB chain" in pdb_lines[0]:
        print("pdb has been adjusted")
    else:
        print("Checking file %s, chain is %s" %(pdb_id, filename[-5]))
        with open("PDBFiles/%s.pdb"%pdb_id, "w+") as pdb_file:
            atom_records = pdbp.one_chain_pdb(pdb_lines, filename[-5])
            if pdb_seq[0:20] == sequence[0:20]:
                #print("Same seq")
                atom_records = pdbp.renumber_pdb_inplace(atom_records, 1)
            else:
                interupt = sequence.split(pdb_seq[0:20])
                #print(len(interupt[0]))
                atom_records = pdbp.renumber_pdb_inplace(atom_records, len(interupt[0])+1)
            pdb_file.write("HEADER    PDB chain %s \t May 9, 2018\n"%pdb_id)
            pdb_file.write("REMARK    Sequence of PDB:\n")
            sequence = textwrap.wrap(sequence, 50)
            for x in sequence:
                pdb_file.write("REMARK    %s\n"%x)
            for value in atom_records:
                pdb_file.write(value)