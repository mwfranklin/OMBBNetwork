import glob

barrels = ["5wq7_A", "5wq8_A", "5tcq_A"]
with open("BarrelChars85.txt", "r") as barrel_data:
    for line in barrel_data:
        if "PDB" not in line:
            line = line.split("\t")
            barrels.append(line[0])

non_barrels = {}
non_barrel_count = 0
with open("data/AllDataE1_v6_Numbered.txt", "r") as inData:
    for line in inData:
        if "Dom1" not in line:
            line = line.split(" ")
            #print(line)
            if line[1] not in barrels:
                non_barrel_count +=1
                if line[1] not in non_barrels.keys():
                    non_barrels[line[1]] = float(line[3])
                elif non_barrels[line[1]] > float(line[3]):
                    non_barrels[line[1]] = float(line[3])
            elif line[2] not in barrels:
                non_barrel_count +=1
                if line[2] not in non_barrels.keys():
                    non_barrels[line[2]] = float(line[3])
                elif non_barrels[line[2]] > float(line[3]):
                    non_barrels[line[2]] = float(line[3])
#print(non_barrels)
print(non_barrel_count)
with open("NonOMBBEValues.txt", "w+") as outData:
    outData.write("PDB\tMin_EValue\n")
    for value in sorted(non_barrels.keys()):
        outData.write(value + "\t" + str(non_barrels[value]) + "\n")
    for value in barrels:
        outData.write(value + "\t" + str(0) + "\n")