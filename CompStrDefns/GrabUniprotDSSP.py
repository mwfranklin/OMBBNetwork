import os
import subprocess
import numpy as np

protos = []
with open("../CompCodesE-3.txt", "r") as barrel_codes:
    for line in barrel_codes:
        line = line.strip().split("\t")
        if line[1] == "1":
            protos.append(line[0])

proto_IDs = {}
for entry in protos:
    print(entry)
    try:
        same_barrels = subprocess.check_output(["grep", entry[0:4], "pdb_chain_uniprot_092618.csv"])
        same_barrels = same_barrels.decode("utf-8").strip().split("\n")
        #print(same_barrels)
        for line in same_barrels:
            line = line.split(",")
            if line[1] == entry[-1]: 
                uniprot_id = line[2]
        same_barrels = subprocess.check_output(["grep", uniprot_id, "pdb_chain_uniprot_092618.csv"])
        same_barrels = same_barrels.decode("utf-8").strip().split("\n")
        same_barrels = [x.split(",") for x in same_barrels]
        to_save = []
        for pdb in same_barrels:
            to_save.append("_".join(pdb[0:2]))
            """if os.path.isfile("DSSP/%s.dssp" %pdb[0]) == False:
                try:
                    os.system("wget -q ftp://ftp.cmbi.ru.nl/pub/molbio/data/dssp/%s.dssp" %pdb[0])
                except:
                    print("Can't get" + pdb[0])
                    continue"""
        only_pdbs = sorted(set([x.split("_")[0] for x in to_save]))
        if len(only_pdbs) == 1:
            continue
        else:
            #print(only_pdbs)
            keep_pdbs = []
            for value in only_pdbs:
                keep_pdbs.append( to_save[ min(i for i,j in enumerate(to_save) if value in j) ] )
            barrels[line[0]] = keep_pdbs
            #print(keep_pdbs)
            proto_IDs[entry] = [uniprot_id, ",".join(keep_pdbs)]

    except subprocess.CalledProcessError:
        print("This PDB isn't mapped to uniprot", entry)

#print(proto_IDs)

with open("UniProtMapping_v5.txt", "w+") as outData:
    for value in sorted(proto_IDs.keys()):
        outData.write(value + "\t" + "\t".join(proto_IDs[value]) + "\n")

