import os
import shutil
from collections import Counter

all_pdb_ids = []
"""with open("data/rawData_E20_v6_2018.txt", "w+") as outdata:
    outdata.write("dom1\tdom2\tE-value\tlength\tPercID\tPercSim\tstart1\tend1\tstart2\tend2\tSeq1\tSeq2\tHHSearchProb\tHHScore\trmsd\ttmscore\tmaxsub\tgdtts\tgdtha\n")
    with open("data/all.flat.d", "r") as inData:
        for line in inData:
            line = line.split(" ")
            if line[0][0:4].upper() == line[1][0:4].upper():
                print(line[0:2])
                continue
            elif float(line[2])< 20: 
                line[0] = line[0][0:4].lower() + line[0][4:]
                line[1] = line[1][0:4].lower()  + line[1][4:]
                all_pdb_ids.append(line[0])
                all_pdb_ids.append(line[1])
                outdata.write("\t".join(line[:6]) + "\t"+ "\t".join(line[7:15]))# + "\t"+ "\t".join(line[21:]))
    with open("data/all136_vs_all136.flt", "r") as inData:
        for line in inData:
            line = line.split(" ")
            if line[0][0:4].upper() == line[1][0:4].upper():
                print(line[0:2])
                continue
            elif float(line[2])< 20: 
                line[0] = line[0][0:4].lower() + line[0][4:]
                line[1] = line[1][0:4].lower()  + line[1][4:]
                all_pdb_ids.append(line[0])
                all_pdb_ids.append(line[1])
                outdata.write("\t".join(line[:6]) + "\t"+ "\t".join(line[7:15]))# + "\t"+ "\t".join(line[21:]))
    with open("data/struct.no_filtering", "r") as inData:
        for line in inData:
            line = line.strip().split(" ")
            if line[0][0:4].upper() == line[1][0:4].upper():
                print(line[0:2])
                continue
            elif float(line[2])< 20 and line[15] != "ERR" and "empty" not in line: 
                line[0] = line[0][0:4].lower() + line[0][4:]
                line[1] = line[1][0:4].lower()  + line[1][4:]
                all_pdb_ids.append(line[0])
                all_pdb_ids.append(line[1])
                outdata.write("\t".join(line[:6]) + "\t"+ "\t".join(line[7:15])+ "\t"+ "\t".join(line[21:]) + "\n")"""
    
with open("v4DB_olddata/struct.no_filtering", "r") as inData:
    for line in inData:
        line = line.strip().split(" ")
        if line[0][0:4].upper() == line[1][0:4].upper():
            print(line[0:2])
            continue
        elif float(line[2])< 20 and line[15] != "ERR" and "empty" not in line: 
            line[0] = line[0][0:4].lower() + line[0][4:]
            line[1] = line[1][0:4].lower()  + line[1][4:]
            all_pdb_ids.append(line[0])
            all_pdb_ids.append(line[1])

all_pdb_ids.extend(["5nec_A", "5fvn_A", "6ehd_A", "6ehb_A", "5nxr_A", "5mdo_A", "5o65_A", "5iv9_A", "5m9b_A"])
        
all_pdb_ids = sorted(set(all_pdb_ids))
all_pdb_ids_no_chain = [x[0:4] for x in all_pdb_ids]
possible_dups = Counter(all_pdb_ids_no_chain)
for value in possible_dups:
    if possible_dups[value] != 1:
        print(value)

#Make incorrect fragment list from the printed statements above; also manually check entries in the rawdata file for sequence identities > 80%

for pdb_id in all_pdb_ids:
    if os.path.isfile("PDBFiles/%s.pdb" %pdb_id) == True:
        #print("File exists %s"%pdb_id)
        continue
    elif os.path.isfile("/Volumes/G_Drive/StructureAlign/NirBenTal/Joanna_and_Meghan/v4_July/pdb_files/%s.pdb"%pdb_id) == True:
        #print("In July pdbs %s"%pdb_id)
        shutil.copy("/Volumes/G_Drive/StructureAlign/NirBenTal/Joanna_and_Meghan/v4_July/pdb_files/%s.pdb"%pdb_id, "PDBFiles/%s.pdb"%pdb_id)
    elif os.path.isfile("/Volumes/G_Drive/StructureAlign/NirBenTal/pdb70_29Apr17.pdb/%s.pdb"%pdb_id) == True:
        #print("In Soding pdbs %s"%pdb_id)
        shutil.copy("/Volumes/G_Drive/StructureAlign/NirBenTal/pdb70_29Apr17.pdb/%s.pdb"%pdb_id, "PDBFiles/%s.pdb"%pdb_id)
    else:
        print("Downloading %s" %pdb_id)
        os.system("curl https://files.rcsb.org/download/%s.pdb -o PDBFiles/%s.pdb" %(pdb_id[0:4], pdb_id))
            