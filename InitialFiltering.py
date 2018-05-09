import os
import shutil

all_pdb_ids = []
with open("all.flat.d", "r") as in_data, open("rawData_E20_v6_2018.txt", "w") as outdata:
    for line in in_data:
        """line = line.replace("3vu1_B", "3vu1_A")
        line = line.replace("3a2s_A", "3a2s_X")
        line = line.replace("5dl8_A", "5dl8_B")
        
        line = line.replace("5AZS_C", "5azs_A")
        line = line.replace("5AZP_C", "5azp_A")
        line = line.replace("4MT4_C", "4mt4_A")
        line = line.replace("3D5K_C", "3d5k_A")        
        line = line.replace("1EK9_B", "1ek9_A") """
        
        line = line.split(" ")
        if line[0][0:4].upper() == line[1][0:4].upper():
            print(line[0:2])
            continue
        elif float(line[2])< 20: 
            line[0] = line[0][0:4].lower() + line[0][4:]
            line[1] = line[1][0:4].lower()  + line[1][4:]
            all_pdb_ids.append(line[0])
            all_pdb_ids.append(line[1])
            outdata.write("\t".join(line[:18]))# + "\t"+ "\t".join(line[21:]))

all_pdb_ids = sorted(set(all_pdb_ids))
for pdb_id in all_pdb_ids:
    if os.path.isfile("PDBFiles/%s.pdb" %pdb_id) == True:
        print("File exists %s"%pdb_id)
    elif os.path.isfile("/Volumes/G_Drive/StructureAlign/NirBenTal/Joanna_and_Meghan/v4_July/pdb_files/%s.pdb"%pdb_id) == True:
        print("In July pdbs %s"%pdb_id)
        shutil.copy("/Volumes/G_Drive/StructureAlign/NirBenTal/Joanna_and_Meghan/v4_July/pdb_files/%s.pdb"%pdb_id, "PDBFiles/%s.pdb"%pdb_id)
    elif os.path.isfile("/Volumes/G_Drive/StructureAlign/NirBenTal/pdb70_29Apr17.pdb/%s.pdb"%pdb_id) == True:
        print("In Soding pdbs %s"%pdb_id)
        shutil.copy("/Volumes/G_Drive/StructureAlign/NirBenTal/pdb70_29Apr17.pdb/%s.pdb"%pdb_id, "PDBFiles/%s.pdb"%pdb_id)
    else:
        print("Downloading %s" %pdb_id)
        os.system("curl https://files.rcsb.org/download/%s.pdb -o PDBFiles/%s.pdb" %(pdb_id[0:4], pdb_id))
            