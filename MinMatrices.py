from collections import Counter
import re
import glob
import sys
import numpy as np

component_labels = ["Other", "Prototypical", "Hemolysins", "Efflux", "Assembly", "Fim/Usher", "Injectisomes", "Adhesins", "Sugar Porins","LptD"]

barrel_codes = {}
with open("CompCodesE<1.txt", "r") as component_file:
    for line in component_file:
        if "PDB" not in line:
            line = line.strip().split("\t")
            barrel_codes[line[0]] = int(line[1])
#print(barrel_codes)

others = [value for value in barrel_codes.keys() if barrel_codes[value] == 0]
#print(others)
min_others = np.full([10, len(others)], 600, dtype=float)
#print(min_others)
min_values = np.full([10,10], 600, dtype=float)
#print(min_values)

with open("FiltData_E20_v6_2018_Renumb_noStructure.txt", "r") as inData:
    for line in inData:
        if "dom1" not in line:
            line = line.strip().split("\t")
            dom1 = line[0]
            dom2 = line[1]
            e_value = float(line[2])        
        
            if (dom1 in barrel_codes.keys() and dom2 in barrel_codes.keys()):
                #print(dom1, dom2)
                if e_value < min_values[barrel_codes[dom1]][barrel_codes[dom2]]:
                    min_values[barrel_codes[dom1]][barrel_codes[dom2]] = e_value
                    min_values[barrel_codes[dom2]][barrel_codes[dom1]] = e_value
                    #print(dom1, dom2, e_value, min_values[barrel_codes[dom2]][barrel_codes[dom1]])
                if dom1 in others: 
                    #print(dom1, dom2, e_value, others.index(dom1), barrel_codes[dom2])
                    if e_value < min_others[barrel_codes[dom2]][others.index(dom1)]:
                        min_others[barrel_codes[dom2]][others.index(dom1)] = e_value
                if dom2 in others:
                    #print(dom1, dom2, e_value, barrel_codes[dom1], others.index(dom2))
                    if e_value < min_others[barrel_codes[dom1]][others.index(dom2)]:
                        min_others[barrel_codes[dom1]][others.index(dom2)] = e_value

#print(min_others)
#print(min_values)
with open("MinMatrixE<1_Prelim.txt", "w+") as outData:
    outData.write("\t".join(component_labels) + "\n")
    for x in min_values:
        outData.write("\t".join(map(str, x)) + "\n")
    outData.write("\n")
    outData.write("\t".join(others) + "\n")
    for x in min_others:
        outData.write("\t".join(map(str, x)) + "\n")

"""with open("v4_July/rawData_E20_v4_July_Renumb.txt", "r") as inData, open("v4_July/MinMatrixTest.txt", "w+") as outData:
    for line in inData:
        if "dom1" not in line:
            line = line.strip().split("\t")
            dom1 = line[0]
            dom2 = line[1]
            e_value = float(line[2])        
        
            if (dom1 in barrel_codes.keys() and dom2 in barrel_codes.keys() and e_value > 1):
                if barrel_codes[dom1] == barrel_codes[dom2]: continue
                elif dom1 in others: continue
                elif dom2 in others: continue
                else:
                    outData.write("\t".join(line) + "\n")"""             