import os
import glob
from collections import Counter
import PDBmanip as pdbm

def define_strands(filename, chainID):
    strands = []
    with open(filename, "r") as origFile:
        this_strand = ""
        this_strand_num = 999
        for line in origFile:
            if "Res" not in line:
                line = line.split("\t")
                if line[3] == chainID:
                    if line[2] == this_strand_num:
                        this_strand += oneletAA[aa.index(line[0])]
                    elif len(this_strand) > 0:
                        strands.append(this_strand)
                        this_strand = oneletAA[aa.index(line[0])]
                    this_strand_num = line[2]
        strands.append(this_strand)
    return(strands)

def get_strands(pdb_id, aligned_res, res_pair_dict):
    #only strands with 3+ res get added to list of aligned strands
    if os.path.isfile("InOut/InOut_%s.txt"%pdb_id[0:4].upper()):
        filename = "InOut/InOut_%s.txt"%pdb_id[0:4].upper()
    elif os.path.isfile("../InOut/InOut_%s.txt"%pdb_id[0:4].upper()):
        filename = "../InOut/InOut_%s.txt"%pdb_id[0:4].upper()
    else:
        print("No InOut file", pdb_id)
        return aligned_res
    
    if pdb_id in res_pair_dict.keys():
        print("checking aligned res", pdb_id)
        #print(aligned_res)
        new_res = [i for i, x in enumerate(res_pair_dict[pdb_id][0]) if x in aligned_res]
        aligned_res = [res_pair_dict[pdb_id][1][x] for x in new_res]
        #print(aligned_res)
    
    strand_res1 = []
    with open(filename, "r") as pdb1_strands:
        for row in pdb1_strands:
            if "Res" not in row:
                row = row.split("\t")
                if row[3].strip() == pdb_id[-1]:
                    if row[1] in aligned_res:
                        strand_res1.append(int(row[2]))
    
    strand_lengths1 = Counter(strand_res1)
    for entry in Counter(strand_res1).keys():
        if Counter(strand_res1)[entry] <= 2:
            del strand_lengths1[entry]
    strand_res1 = sorted(set(strand_lengths1.keys()))
    strand_res1 = ["strand"+str(x) for x in strand_res1]
    
    #print(strand_res1)        
    return strand_res1

aa = ["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL", "MSE", "SEC"]
oneletAA = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]

barrels = {}
with open("DSSP_GT5.txt", "r") as inData:
    for line in inData:
        line = line.strip().split("\t")
        barrels[line[0]] = line[2:]

alt_chains = {}
for x in barrels.keys():
    barrels[x] = [y for y in barrels[x] if "_" in y]
    for entry in barrels[x]:
        alt_chains[entry[0:4]] = entry[-1]

alt_strands = {}
for filename in glob.glob("InOut/*.txt"):
    pdb_id = filename.split("/")[-1][6:-4].lower()
    #print(pdb_id, alt_chains[pdb_id])
    alt_strands[pdb_id] = define_strands(filename, chainID = alt_chains[pdb_id])

best_structures = {}    
for x in barrels.keys():
    shortest = x
    longest = x
    orig_strands = define_strands("../InOut/InOut_%s.txt"%x[0:4].upper(), chainID = x[-1])
    #print(orig_strands)
    for entry in barrels[x]:
        if len(set(orig_strands) & set(alt_strands[entry[0:4]])) == len(orig_strands):
            continue
        elif sum([len(x) for x in orig_strands]) < sum([len(x) for x in alt_strands[entry[0:4]]]):
            longest = entry
        elif sum([len(x) for x in orig_strands]) > sum([len(x) for x in alt_strands[entry[0:4]]]):
            shortest = entry
        best_structures[x] = [longest, shortest]
    if len(orig_strands) == 16 or len(orig_strands) == 18:
        try:
            print(x, len(orig_strands), best_structures[x])
        except:
            continue
with open("BestAltStructures.txt", "w+") as outData:
    outData.write("Orig\tLong\tShort\n")
    for x in best_structures.keys():
        outData.write(x + "\t" + "\t".join(best_structures[x]) + "\n")


aligned_res_ids = {}
for x in best_structures.keys():
    with open("../PDBFiles/%s.pdb"%x, "r") as x_file:
        x_file = x_file.readlines()
    seq_x = pdbm.seq_from_struct(x_file, x[-1])
    x_res = []
    for line in x_file:
        if line[0:4] == "ATOM" and line[12:16].strip() == "CA"and line[21] == x[-1] and line[16] in [" ", "A", "1"]:
            x_res.append(line[22:26].strip())
        elif line[0:6] == "HETATM" and line[12:16].strip() == "CA" and line[17:20] in aa and line[21] == x[-1] and line[16] in [" ", "A", "1"]:
            x_res.append(line[22:26].strip())
        elif "ENDMDL" in line: break
        
    for entry in best_structures[x]:
        if entry != x:
            #print(x, entry)
            new_x_res = x_res[:]
            with open("CompPDBs/%s.pdb"%entry[0:4], "r") as entry_file:
                entry_file = entry_file.readlines()
            seq_entry = pdbm.seq_from_struct(entry_file, entry[-1])
            #print(seq_entry)
            entry_res = []
            for line in entry_file:
                if line[0:4] == "ATOM" and line[12:16].strip() == "CA"and line[21] == entry[-1] and line[16] in [" ", "A", "1"]:
                    entry_res.append(line[22:26].strip())
                elif line[0:6] == "HETATM" and line[12:16].strip() == "CA" and line[17:20] in aa and line[21] == entry[-1] and line[16] in [" ", "A", "1"]:
                    entry_res.append(line[22:26].strip())
                elif "ENDMDL" in line: break
                elif "TER" in line[0:3]: break
            seq_x_new, seq_entry = pdbm.align_seq(seq_x, seq_entry)
            #print("".join(seq_x_new))
            #print("".join(seq_entry))
            
            k = 0
            while k <= len(seq_x_new)-1:
                if seq_x_new[k] == "-":
                    new_x_res.insert(k, "-")
                if seq_entry[k] == "-":
                    entry_res.insert(k, "-")
                k+= 1
            if new_x_res[5] == entry_res[5] and new_x_res[-5] == entry_res[-5]: continue
            elif new_x_res[27] == entry_res[27] and new_x_res[-5] == entry_res[-5]: continue
            else:
                #print(x, entry, len(new_x_res), len(entry_res))
                if len(new_x_res) != len(entry_res):
                    print(x, entry, len(new_x_res), len(entry_res))
                    #print(new_x_res)
                    #print(entry_res)
                k = len(seq_x_new) - 1
                while k > 0:
                    if new_x_res[k] == "-" and entry_res[k] == "-":
                        del new_x_res[k]
                        del entry_res[k]
                    k -= 1
                #print(x_res)
                #print(entry_res)
                aligned_res_ids[entry] = [new_x_res, entry_res]

with open("../data/AllDataE1_v6_Numbered.txt", "r") as inData, open("../data/AllDataE1_v6_Numbered_Longest.txt", "w+") as longest_out, open("../data/AllDataE1_v6_Numbered_Shortest.txt", "w+") as shortest_out:
    for line in inData:
        if "Dom1" in line:
            longest_out.write(line)
            shortest_out.write(line)
        else:
            line = line.split(" ")
            pdb1 = line[1]
            pdb2 = line[2]
            start1 = int(line[4].split("-")[0])
            start2 = int(line[5].split("-")[0])
            seq1 = line[8]
            seq2 = line[9]
            
            count1 = 0
            count2 = 0
            res1 = []
            res2 = []
            print(pdb1, pdb2)#, len(seq1), len(seq2))
            for x in range(0, len(seq1)):
                if seq1[x] == "-": 
                    #print("GAP", seq1[x], seq2[x], count2 + start2)
                    count2 += 1
                elif seq2[x] == "-":
                    #print("GAP", seq1[x], seq2[x], count1 + start1)
                    count1 += 1
                else:
                    res1.append(start1 + count1)
                    res2.append(start2 + count2)
                    count1 +=1
                    count2 +=1
            res1 = [str(x) for x in res1]
            res2 = [str(x) for x in res2]
            
            strands1 = get_strands(pdb1, res1, aligned_res_ids)
            strands2 = get_strands(pdb2, res2, aligned_res_ids)
            if pdb1 in best_structures.keys():
                strands1_short = get_strands(best_structures[pdb1][1], res1, aligned_res_ids)
                strands1_long = get_strands(best_structures[pdb1][0], res1, aligned_res_ids)
                if len(set(strands1) & set(strands1_short)) != len(strands1):
                    print("short", best_structures[pdb1][1], line[0:3], strands1, strands1_short)
                if len(set(strands1) & set(strands1_long)) != len(strands1):
                    print("long", best_structures[pdb1][0], line[0:3], strands1, strands1_long)
            else:
                strands1_short = strands1
                strands1_long = strands1
            
            if pdb2 in best_structures.keys():
                strands2_short = get_strands(best_structures[pdb2][1], res2, aligned_res_ids)
                strands2_long = get_strands(best_structures[pdb2][0], res2, aligned_res_ids)
                if len(set(strands2) & set(strands2_short)) != len(strands2):
                    print("short", best_structures[pdb2][1], line[0:3], strands2, strands2_short)
                if len(set(strands2) & set(strands2_long)) != len(strands2):
                    print("long", best_structures[pdb2][0], line[0:3], strands2, strands2_long)
            else:
                strands2_short = strands2
                strands2_long = strands2
            
            
            longest_out.write("%s %s %s %s"%(" ".join(line[0:6]), ",".join(map(str, strands1_long)), ",".join(map(str, strands2_long)), " ".join(line[8:])) )
            shortest_out.write("%s %s %s %s"%(" ".join(line[0:6]), ",".join(map(str, strands1_short)), ",".join(map(str, strands2_short)), " ".join(line[8:])) )

