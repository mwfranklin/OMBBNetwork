import os

with open("data/ProtosOnlyE-3_v6_Numbered.txt", "r") as inData, open("data/ProtosOnlyE-3_v6_Numbered_Tabbed.txt", "w+") as outData:
    for line in inData:
        line = line.split(" ")
        outData.write("\t".join(line))