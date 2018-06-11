import os
import shutil
import glob
import PDBparser as pdbp
import textwrap

inject = ["5tcq_A", "5wq8_A", "5wq7_A"]

for value in inject:
    with open("PDBFiles/%s.pdb"%value, "r") as pdb_file:
        pdb_lines = pdb_file.readlines()
    sequence = pdbp.pdb_to_seq(pdb_lines)
    pdb_seq = pdbp.seq_from_struct(pdb_lines)
    with open("PDBFiles/%s.pdb"%value, "w+") as pdb_file:
        atom_records = pdbp.one_chain_pdb(pdb_lines, "A")
        atom_records = pdbp.renumber_pdb_Rosetta(atom_records, value + ".pdb", 1)
        #for entry in atom_records:
         #   pdb_file.write(entry)