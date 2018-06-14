import os
import re
import glob

def get_combos(list1, list2):
    uniques1 = set(list1).difference(list2)
    uniques2 = set(list2).difference(list1)
    both_sets = set(list1).intersection(list2)
    print("a, b, same", len(uniques1), len(uniques2), len(both_sets))
    combos_possible = len(uniques1)*len(uniques2) + len(both_sets)*(len(uniques1)+len(uniques2))
    return combos_possible

all_barrels = {}
with open("BarrelChars85.txt", "r") as barrel_data:
  for line in barrel_data:
    if "PDB" not in line:
      line = line.strip().split()
      all_barrels[line[0]] = int(line[1])

all_prototypicals = []
with open("CompCodesE-3.txt", "r") as inData:
    for line in inData:
        if "PDB" not in line:
            line = line.strip().split("\t")
            if line[1] == "1": all_prototypicals.append(line[0])

proto_hom = {}
all_hits_by_size = [ [] for x in range(27) ]
all_hits = []
for filename in glob.glob("MSAs/*.a3m"):
    pdb_id = filename.split("/")[-1][:-4]
    pdb_id = pdb_id[0:4].lower() + pdb_id[4:]
    a3m_list = []
    if pdb_id in all_prototypicals:
        #print(pdb_id)
        with open(filename, "r") as inData:
            for line in inData:
                if ">tr|" in line:
                    new_id = line.split("|")[1]
                    a3m_list.append(new_id)
        all_hits_by_size[ all_barrels[pdb_id] ].extend(a3m_list)
        proto_hom[ pdb_id ] = a3m_list
        all_hits.extend(a3m_list)
        
        """with open("MSAs/%s.hhm"%pdb_id, "r") as hhm_file:
            for line in hhm_file:
                if "FILT" in line:
                    print(line.strip())
                    print(len(a3m_list))"""

print(len(all_hits), len(set(all_hits)))
#all_hits_by_size = [set(x) for x in all_hits_by_size]
#print([len(x) for x in all_hits_by_size])

"""set_diffs = np.zeros([23,23])
for x in range(8,23):
    for y in range(x+1, 23):
        set_diffs[x][y] = len(set(all_hits_by_size[x]).intersection(all_hits_by_size[y]))
print(set_diffs)
with open("HomoIntersections.txt", "w+") as outData:
    for x in range(8,23):
        outData.write(str(x) + "\t" + "\t".join(map(str, set_diffs[x])) + "\n")"""

#this section is a slimmed down version of BtwnBarrelMetric.py to get at the combinations possible between 
allowed_barrels = []
with open("/Users/meghan/Documents/PhD/SluskyLab/DBList_v5_85_Chains.txt", "r") as allowed_data:
    for line in allowed_data:
        allowed_barrels.append(line.strip())
prototypical = set(allowed_barrels).intersection(all_prototypicals)
print(len(prototypical))

diff_barrel_lines = [ [ [] for i in range(27)] for j in range(27)]
with open("data/AllDataE1_v6_Numbered.txt", "r") as inData:
    for line in inData:
        if "IntNum" not in line:
            line = line.strip().split()
            if line[1] in prototypical and line[2] in prototypical and float(line[3]) <= 1e-3:# and line[-1] == "1": #add line[-1] == "1" for min e-value calcs; change float(line[3]) to 1e-5 for tree diagram
                keep_piece = line[0:4] + line[6:8]
                diff_barrel_lines[ all_barrels[line[1]]][ all_barrels[line[2]] ].append(keep_piece)
                diff_barrel_lines[ all_barrels[line[2]]][ all_barrels[line[1]] ].append(keep_piece)
    
for x in range(8,23):
    for y in range(x, 23):
        if len(diff_barrel_lines[x][y]) > 1:
            diff_barrel_lines[x][y] = [list(i) for i in set(tuple(i) for i in diff_barrel_lines[x][y])]
            for entry in diff_barrel_lines[x][y]:
                #print(entry)
                entry[4] = re.split(",", entry[4])
                entry[5] = re.split(",", entry[5])
                if len(entry[4]) > 1:
                    entry[4] = sorted([int(x.split("strand")[-1]) for x in entry[4]])
                else: entry[4] = []
                if len(entry[5]) > 1:
                    entry[5] = sorted([int(x.split("strand")[-1]) for x in entry[5]])
                else: entry[5] = []

c_term_barrels = [[] for x in range(23)]
n_term_barrels = [[] for x in range(23)]
for x in range(16,17):
    for y in range(x+1, 23):
        if len(diff_barrel_lines[x][y]) > 1:
            print(x, y, "total aligns:",len(diff_barrel_lines[x][y]))
            c_terminal_align = 0
            n_terminal_align = 0
            double_hairpin = 0
            non_hairpins = []
            barrels_x = []
            barrels_y = []
            for entry in diff_barrel_lines[x][y]:              
                #identify any alignments between c-terminal strands or falling into that pattern
                if len(entry[4]) != len(entry[5]):
                    print("diff lengths", entry)
                    non_hairpins.append(entry[0])
                elif abs(entry[4][-1] - entry[5][-1]) == abs(all_barrels[entry[1]] - all_barrels[entry[2]]):
                    #print("Terminal Align", entry)
                    c_terminal_align += 1
                    c_term_barrels[all_barrels[entry[1]] ].append(entry[1])
                    c_term_barrels[all_barrels[entry[2]] ].append(entry[2])
                elif entry[4][0] == entry[5][0]:
                    #print("N-Terminal Align", entry)
                    n_terminal_align += 1
                    
                elif abs(entry[4][-1] - entry[5][-1]) == 4:
                    print("Double-hairpin Align", entry)
                    n_term_barrels[all_barrels[entry[1]] ].append(entry[1])
                    n_term_barrels[all_barrels[entry[2]] ].append(entry[2])
                    double_hairpin += 1
                else:
                    print("nonhairpin", entry)
                    non_hairpins.append(entry[0])
                
            print(c_terminal_align, n_terminal_align, double_hairpin, len(non_hairpins))
c_term_barrels = [set(x) for x in c_term_barrels]
n_term_barrels = [set(x) for x in n_term_barrels]

c_term_homo = [[] for x in range(23)]
for x in range(23):
    for entry in c_term_barrels[x]:
        c_term_homo[x].extend(proto_hom[entry])
    c_term_homo[x] = sorted(set(c_term_homo[x]))

n_term_homo = [[] for x in range(23)]
for x in range(23):
    for entry in n_term_barrels[x]:
        n_term_homo[x].extend(proto_hom[entry])
    n_term_homo[x] = sorted(set(n_term_homo[x]))

eight_10 = get_combos(c_term_homo[8], c_term_homo[10])
eight_12 = get_combos(c_term_homo[8], c_term_homo[12])
eight_14 = get_combos(c_term_homo[8], c_term_homo[14])
eight_16 = get_combos(c_term_homo[8], c_term_homo[16])
eight_10+eight_12+eight_14+eight_16

ten_12 = get_combos(c_term_homo[10], c_term_homo[12])
twelve_14 = get_combos(c_term_homo[12], c_term_homo[14])
twelve_16 = get_combos(c_term_homo[10], c_term_homo[16])
ten_12+twelve_14+twelve_16

sixteen_18 = get_combos(c_term_homo[16], c_term_homo[18])
sixteen_18_n = get_combos(n_term_homo[16], n_term_homo[18])


lg_rearr = ["1pho_A", "2por_A", "2zfg_A", "3nsg_A", "5fvn_A", "5nxr_A", "4d65_A"]
lg_rearr_16 = []
for x in lg_rearr:
    lg_rearr_16.extend(proto_hom[x])
lg_rearr_16 = sorted(set(lg_rearr_16))
len(lg_rearr_16)
sixteen_18_lg = get_combos(lg_rearr_16, proto_hom["5ldv_A"])
print(sixteen_18_lg)

loop_hairpin_16 = ["4aui_A", "6ehd_A", "3wi5_A", "3prn_A"]
hairpin_loop_16 = ["3prn_A", "2fgr_A", "6ehb_A"]
hairpin_loop_18 = ["3sy7_A", "3szd_A", "4frx_A", "5dl5_A", "4fsp_A", "4fso_A"]
hairpin_loop_16_walts = ["3prn_A", "6ehb_A"]
hairpin_loop_18_walts = ["3sys_A", "2y0l_A", "4frx_A", "3szv_A", "5dl7_A"]
lh_16 = []
for x in loop_hairpin_16:
    lh_16.extend(proto_hom[x])
lh_16 = sorted(set(lh_16))

hl_16 = []
for x in hairpin_loop_16:
    hl_16.extend(proto_hom[x])
hl_16 = sorted(set(hl_16))
hl_18 = []
for x in hairpin_loop_18:
    hl_18.extend(proto_hom[x])
hl_18 = sorted(set(hl_18))

hl_16_alts = []
for x in hairpin_loop_16_walts:
    hl_16_alts.extend(proto_hom[x])
hl_16_alts = sorted(set(hl_16_alts))
hl_18_alts = []
for x in hairpin_loop_18_walts:
    hl_18_alts.extend(proto_hom[x])
hl_18_alts = sorted(set(hl_18_alts))

print(get_combos(lh_16, proto_hom["5ldv_A"]))
print(get_combos(hl_16, hl_18))
print(get_combos(hl_16_alts, hl_18_alts))
