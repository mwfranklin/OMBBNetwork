import numpy as np
import glob
import matplotlib.pyplot as plt
import scipy.stats

aa = ["GLY", "PRO", "ARG","LYS", "HIS","ASN","GLN", "SER","THR","CYS", "ASP","GLU", "PHE","TRP","TYR", "MET","ALA","LEU","ILE","VAL"]
aa_sizes = [48, 90, 148,135, 118,96,114, 73,93,86, 91,109, 135,163,141,  124,67,124,124,105]
aa_avg_group = [48, 90, 141.5,141.5, 109.3,109.3,109.3, 84,84,84, 100,100, 146.3,146.3,146.3, 108.8,108.8,108.8,108.8,108.8]

protos = []
with open("CompCodesE-3.txt", "r") as inData:
    for line in inData:
        if "PDB" not in line:
            line = line.strip().split("\t")
            if line[1] == "1": protos.append(line[0])

barrels = {}
with open("BarrelChars85.txt", "r") as inData:
    for line in inData:
        if "PDB" not in line:
            line = line.split("\t")
            if line[0] in protos:
                barrels[line[0]] = [int(line[1])]

all_avgs = [[] for x in range(0,23)]
for key in barrels.keys():
    print(key)
    in_aa = np.zeros(20)
    out_aa = np.zeros(20)
    with open("InOut/InOut_%s.txt"%key[0:4].upper(), "r") as inData:
        for line in inData:
            if "Res" in line:
                continue
            else:
                line = line.split("\t")
                if line[3] == key[-1]:
                    if line[4] == "True":
                        in_aa[aa.index(line[0])] += 1
                    else:
                        out_aa[aa.index(line[0])] += 1
    in_aa_avg = sum(in_aa*aa_sizes)/sum(in_aa)
    out_aa_avg = sum(out_aa*aa_sizes)/sum(out_aa)
    in_aa_avg_noGly = sum(in_aa[1:]*aa_sizes[1:])/sum(in_aa[1:])
    out_aa_avg_noGly = sum(out_aa[1:]*aa_sizes[1:])/sum(out_aa[1:])
    perc_gly = in_aa[0]+out_aa[0]/sum(in_aa + out_aa)
    all_avgs[barrels[key][0]].append([in_aa_avg, out_aa_avg, in_aa_avg_noGly, out_aa_avg_noGly, perc_gly])
    barrels[key].extend([in_aa_avg, out_aa_avg, in_aa_avg_noGly, out_aa_avg_noGly, perc_gly])

sc_sizes = np.array(list(barrels.values()))
new_avgs = []
for x in range(0,23):
    all_avgs[x] = np.asarray(all_avgs[x])
    if len(all_avgs[x]) > 0:
        new_avgs.append(np.mean(all_avgs[x], axis = 0))
new_avgs = np.asarray(new_avgs)
barrel_sizes = [8,10,12,14,16,18,22]


#r2_labels = [98.5, 111] #for aa_avg
#r2_labels = [101, 111] #for aa_avg_group
r2_labels = [99.5, 109] #for noGly
fig, ax1 = plt.subplots(nrows = 1, ncols= 1, figsize = (7,7))
ax1.scatter(barrel_sizes, new_avgs[:,0], c = "blue", marker = "o", label = "Inward", alpha=0.8)
these_stats = scipy.stats.linregress(barrel_sizes, new_avgs[:,0])
#print(these_stats)
ax1.plot(np.arange(6,25,0.5), these_stats.slope*np.arange(6,25,0.5) + these_stats.intercept, c = "blue")
ax1.annotate(r"$\mathregular{R^2}$=%0.4f"%these_stats.rvalue**2, xy = (18.5, r2_labels[0]), xycoords = "data", size = 16)
#print(these_stats.pvalue)
ax1.scatter(barrel_sizes, new_avgs[:,1], c = "red", marker = "o", label = "Outward", alpha=0.8)
these_stats = scipy.stats.linregress(barrel_sizes, new_avgs[:,1])
#print(these_stats)
ax1.plot(np.arange(6,25,0.5), these_stats.slope*np.arange(6,25,0.5) + these_stats.intercept, c = "red")
ax1.annotate(r"$\mathregular{R^2}$=%0.4f"%these_stats.rvalue**2, xy = (18.5, r2_labels[1]), xycoords = "data", size = 16)
ax1.set_xlim([6,24])
ax1.set_ylabel(r"Average Side Chain Volume ($\AA$)", fontsize = 18)
ax1.set_xlabel("Barrel Size, Strands", fontsize = 18)
ax1.set_title("Average Side Chain Volumes", fontsize = 24)
plt.legend(fontsize = 18, loc = 4)
plt.tick_params(labelsize = 14)
plt.savefig("NetworkGraphs/SCVolumesBarrelAvg.png")

#r2_labels = [98.5, 111] #for aa_avg
#r2_labels = [101, 111] #for aa_avg_group
"""r2_labels = [107, 115] #for noGly
fig, ax1 = plt.subplots(nrows = 1, ncols= 1, figsize = (10,10))
ax1.scatter(sc_sizes[:,0], sc_sizes[:,3], c = "blue", marker = "o", label = "Inward", alpha=0.8)
these_stats = scipy.stats.linregress(sc_sizes[:,0], sc_sizes[:,3])
ax1.plot(np.arange(6,25,0.5), these_stats.slope*np.arange(6,25,0.5) + these_stats.intercept, c = "blue")
ax1.annotate("R2=%0.4f"%these_stats.rvalue**2, xy = (18.5, r2_labels[0]), xycoords = "data", size = 16)
print(these_stats.pvalue)

ax1.scatter(sc_sizes[:,0], sc_sizes[:,4], c = "red", marker = "o", label = "Outward", alpha=0.8)
these_stats = scipy.stats.linregress(sc_sizes[:,0], sc_sizes[:,4])
ax1.plot(np.arange(6,25,0.5), these_stats.slope*np.arange(6,25,0.5) + these_stats.intercept, c = "red")
ax1.annotate("R2=%0.4f"%these_stats.rvalue**2, xy = (18.5, r2_labels[1]), xycoords = "data", size = 16)
print(these_stats.pvalue)
plt.legend(fontsize = 18)

ax2 = ax1.twinx()
ax2.scatter(sc_sizes[:,0]+0.25, sc_sizes[:,5], c = "green", label = "Total Gly %")
these_stats = scipy.stats.linregress(sc_sizes[:,0], sc_sizes[:,5])
ax2.plot(np.arange(6,25,0.5), these_stats.slope*np.arange(6,25,0.5) + these_stats.intercept, c = "green")
ax2.annotate("R2=%0.4f"%these_stats.rvalue**2, xy = (18.5, 16), xycoords = "data", size = 16)
ax2.set_ylabel("Percent Total Gly")

ax1.set_ylabel("Average Side-chain Volume, A", fontsize = 18)
ax1.set_xlabel("Barrel Size", fontsize = 18)
ax1.set_title("Average Side Chain Volumes, No Gly", fontsize = 26)
ax1.set_xlim([6,24])

plt.tick_params(labelsize = 16)
#plt.tight_layout()
plt.savefig("NetworkGraphs/SCVolumesNoGly.png")"""
