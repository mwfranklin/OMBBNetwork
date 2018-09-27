import glob
import os
import subprocess
import pandas as pd

def add_all_dssp(orig_dssp, pdb_list, pdb, barrel_chars):
    for entry in pdb_list:
        #print(pdb, entry)
        if entry == pdb:
            continue
        else:
            start = False
            dssp_defns = [[],[]]
            with open("DSSP/%s.dssp"%entry[0:4], "r") as DSSP_file:
                print(entry)
                for row in DSSP_file:
                    if row[2] == "#": start = True
                    elif start == False: continue
                    else:
                        #print(row[11])
                        if row[11] == entry[-1]:
                            res_id = int(row[5:11].strip())
                            if res_id >= barrel_chars[pdb][0] and res_id <= barrel_chars[pdb][1]:
                                dssp_defns[0].append(res_id)
                                dssp_defns[1].append(row[16])
            dssp_defns = pd.DataFrame(dssp_defns) #, columns = ["Res", pdb_id])
            dssp_defns = dssp_defns.transpose()
            dssp_defns.columns = ["Res", entry]
            orig_dssp = pd.merge(orig_dssp, dssp_defns, on="Res", how = "left")
    return(orig_dssp)


barrel_chars = {}
with open("../BarrelChars85.txt", "r") as inData:
    for line in inData:
        line = line.strip().split("\t")
        if "PDB" not in line:
            barrel_chars[line[0]] = [int(line[4]), int(line[5])]

barrels = {}
keep_data = []
with open("UniProtMapping_v5_test.txt", "r") as inData:
    for line in inData:
        print(line)
        line = line.strip().split("\t")
        pdb_id = line[0]
        start = False
        
        dssp_defns = [[],[]]
        with open("DSSP/%s.dssp"%pdb_id[0:4], "r") as DSSP_file:
            #print(pdb_id)
            for row in DSSP_file:
                if row[2] == "#": start = True
                elif start == False: continue
                else:
                    if row[11] == pdb_id[-1]:
                        res_id = int(row[5:11].strip())
                        if res_id >= barrel_chars[pdb_id][0] and res_id <= barrel_chars[pdb_id][1]:
                            dssp_defns[0].append(res_id)
                            dssp_defns[1].append(row[16])
        dssp_defns = pd.DataFrame(dssp_defns)
        dssp_defns = dssp_defns.transpose()
        dssp_defns.columns = ["Res", pdb_id]
        #print(dssp_defns)
        
        dssp_defns = add_all_dssp(dssp_defns, line[2].split(","), pdb_id, barrel_chars)
        line[2] = line[2].split(",")
        sim_values = []
        for entry in line[2]:
            print(entry)
            if entry == pdb_id: continue
            else:
                perc_diff = 1 - np.size(np.where(dssp_defns[pdb_id] == dssp_defns[entry]))/len(dssp_defns)
                if perc_diff == 1:
                    continue
                elif perc_diff >= 0.05:
                    this_sim = entry+"\t" + str(perc_diff)
                    sim_values.append(this_sim)
        if len(sim_values) > 0:
            keep_data.append([pdb_id, line[1], "\t".join(sim_values)])
        
print(len(keep_data))
with open("DSSP_GT5.txt", "w+") as outData:
    for value in keep_data:
        outData.write("\t".join(value) + "\n")

