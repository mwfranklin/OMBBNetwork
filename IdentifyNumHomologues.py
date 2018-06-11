import os
import re
import glob

all_barrels = {}
with open("BarrelChars85.txt", "r") as barrel_data:
  for line in barrel_data:
    if "PDB" not in line:
      line = line.strip().split()
      all_barrels[line[0].upper()] = int(line[1])

prototypicals = []
with open("CompCodesE-3.txt", "r") as inData:
    for line in inData:
        if "PDB" not in line:
            line = line.strip().split("\t")
            if line[1] == "1": prototypicals.append(line[0].upper())

all_hits_by_size = [ [] for x in range(27) ]
all_hits = []
for filename in glob.glob("MSAs/*.a3m"):
    pdb_id = filename.split("/")[-1][:-4]
    a3m_list = []
    if pdb_id in prototypicals:
        #print(pdb_id)
        with open(filename, "r") as inData:
            for line in inData:
                if ">tr|" in line:
                    new_id = line.split("|")[1]
                    a3m_list.append(new_id)
        all_hits_by_size[ all_barrels[pdb_id] ].extend(a3m_list)
        all_hits.extend(a3m_list)
        
        """with open("MSAs/%s.hhm"%pdb_id, "r") as hhm_file:
            for line in hhm_file:
                if "FILT" in line:
                    print(line.strip())
                    print(len(a3m_list))"""
print(len(all_hits), len(set(all_hits)))

all_hits_by_size = [set(x) for x in all_hits_by_size]
print([len(x) for x in all_hits_by_size])

set_diffs = np.zeros([23,23])
for x in range(8,23):
    for y in range(x+1, 23):
        set_diffs[x][y] = len(set(all_hits_by_size[x]).intersection(all_hits_by_size[y]))
print(set_diffs)
with open("HomoIntersections.txt", "w+") as outData:
    for x in range(8,23):
        outData.write(str(x) + "\t" + "\t".join(map(str, set_diffs[x])) + "\n")


