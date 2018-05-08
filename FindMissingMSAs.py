import os
import re

all_pdbs = []
with open("WholeDB_v4.txt", "r") as inData:
    for line in inData:
        all_pdbs.append(line.strip())

with open("FinishHHMs.txt", "w+") as outData:
    for value in all_pdbs:
        if os.path.isfile("MSAs/%s.hhm"%value) == False:
            outData.write(value + "\n")
