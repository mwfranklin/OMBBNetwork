import os
import sys
import glob
import re
import subprocess

for filename in glob.glob("MSAs/*.a3m"):
    pdb_id = filename.split("/")[-1][:-4]
    os.system("hhalign -i %s -o data/IntRepeats/%s_Score.txt"%(filename, pdb_id))
    
    