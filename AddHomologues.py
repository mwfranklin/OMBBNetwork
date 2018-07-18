import os
import re
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import stats
import numpy as np
import textwrap
import glob

all_barrels = {}
with open("BarrelChars85.txt", "r") as barrel_data:
  for line in barrel_data:
    if "PDB" not in line:
      line = line.strip().split()
      all_barrels[line[0]] = int(line[1])

all_homologues = {}
for filename in glob.glob("MSAs/*.a3m"):
    pdb_id = filename.split("/")[-1][:-4]
    pdb_id = pdb_id[0:4].lower() + pdb_id[4:]
    a3m_list = []
    with open(filename, "r") as inData:
        for line in inData:
            if ">tr|" in line:
                new_id = line.split("|")[1]
                a3m_list.append(new_id)
    all_homologues[ pdb_id ] = a3m_list

homo_sizes = []
with open("data/AllDataE1_v6_Numbered.txt", "r") as inData, open("data/AllDataE1_v6_Numbered_Hom.txt", "w+") as outData, open("data/AllDataE1_v6_Numbered_Hom_Tabbed.txt", "w+") as outDataTab:
    for line in inData:
        line = line.strip().split(" ")
        pdb1 = line[1]
        pdb2 = line[2]
        
        if "interaction" in line:
            #continue
            outData.write(" ".join(line) + " SharedHom TotalHom StrNumChange SameSize\n")
            outDataTab.write("\t".join(line) + "\tSharedHom\tTotalHom\tStrNumChange\tSameSize\n")
        
        elif pdb1 in all_barrels.keys() and pdb2 in all_barrels.keys():
            all_homos = len(set(all_homologues[pdb1] + all_homologues[pdb2]))
            shared_homos = len(set(all_homologues[pdb1]).intersection(all_homologues[pdb2]))
            #homo_sizes.append(shared_homos/all_homos)
            #print(pdb1, pdb2, shared_homos/all_homos)
            strands1 = line[6].split(",")
            strands2 = line[7].split(",")
            if len(strands1) == len(strands2):
                if all_barrels[pdb1] == all_barrels[pdb2]:
                    outData.write(" ".join(line) + " " + str(shared_homos/all_homos) + " "+ str(all_homos) + " 0 1" + "\n")
                    outDataTab.write("\t".join(line) + "\t" + str(shared_homos/all_homos) + "\t" + str(all_homos) + "\t0\t1\n")
                else:
                    outData.write(" ".join(line) + " " + str(shared_homos/all_homos) + " "+ str(all_homos) + " 0 0" + "\n")
                    outDataTab.write("\t".join(line) + "\t" + str(shared_homos/all_homos) + "\t" + str(all_homos) + "\t0\t0\n")
                    homo_sizes.append(shared_homos/all_homos)
            else:
                if all_barrels[pdb1] == all_barrels[pdb2]:
                    outData.write(" ".join(line) + " " + str(shared_homos/all_homos) + " "+ str(all_homos) + " 1 1" + "\n")
                    outDataTab.write("\t".join(line) + "\t" + str(shared_homos/all_homos) + "\t" + str(all_homos) + "\t1\t1\n")
                else:
                    outData.write(" ".join(line) + " " + str(shared_homos/all_homos) + " "+ str(all_homos) + " 1 0" + "\n")
                    outDataTab.write("\t".join(line) + "\t" + str(shared_homos/all_homos) + "\t" + str(all_homos) + "\t1\t0\n")
                #homo_sizes.append(shared_homos/all_homos)
        else:
            #continue
            outData.write(" ".join(line) + " 0 0 0 2\n")
            outDataTab.write("\t".join(line) + "\t0\t0\t0\t2\n")

print(np.mean(homo_sizes))
fig, ax3 = plt.subplots(nrows = 1, ncols = 1, figsize = (8,10))
ax3.set_xlabel("Proportion of shared homologues", size = 22)
ax3.set_ylabel("Density", size = 22)
kde = stats.gaussian_kde(homo_sizes)
xnew = np.arange(0, 1, 0.01)
ax3.plot(xnew, kde.evaluate(xnew), linewidth = 2)
ax3.scatter(homo_sizes, np.full(len(homo_sizes), 0.005), c = "black", s = 50)
#ax3.hist(homo_sizes, bins = np.arange(0,1.1,0.1), histtype = "step", normed = True)
#ax3.annotate("TEST", xy=[60,0.8], xycoords="data", fontsize=30)
#leg = ax3.legend(fontsize = 14, loc = 2)
# set the linewidth of each legend object
#for legobj in leg.legendHandles:
 #   legobj.set_linewidth(2.5)
#ax3.set_ylim([0, 0.85])
#ax3.set_xlim([0,1])
ax3.set_xlim([0,0.05])
plt.tick_params(labelsize = 14)
plt.tight_layout()
plt.savefig("NetworkGraphs/DistribSharedHomologues_DiffBarrelSize.png")
#plt.show()
            