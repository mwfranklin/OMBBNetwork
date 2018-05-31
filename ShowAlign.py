from pymol import cmd, stored
import glob
import re

def show_motif(value):
    cmd.delete("*")
    domain1 = align_pairs[value][0]
    domain2 = align_pairs[value][1]
    residues1 = align_pairs[value][2]
    residues2 = align_pairs[value][3]
    
    cmd.load("PDBFiles/%s.pdb"%domain1)
    cmd.load("PDBFiles/%s.pdb"%domain2)    
    cmd.bg_color("white")
    
    cmd.hide("all")
    cmd.show("cartoon", "all")
    cmd.select("motif1", "none")
    cmd.select("motif1", "motif1 or (%s and n. CA and resi %s)"%(domain1, residues1))
    cmd.select("motif2", "none")
    cmd.select("motif2", "motif2 or (%s and n. CA and resi %s)"%(domain2, residues2))
    cmd.select("none")
    cmd.color("gray80", domain1)
    cmd.color("gray60", domain2)
    cmd.color("cyan", "motif1")
    cmd.color("magenta", "motif2")
    #cmd.seqview("on")
    try:
        cmd.pair_fit("motif1", "motif2", object="alignment")
        cmd.center(domain1)
        #cmd.png("PNGsRenumb/%s_%s_PF.png"%(domain1, domain2), dpi = 300)
    except CmdException:
        pass
    
    try: 
        cmd.cealign("motif1", "motif2", object="alignment")
        cmd.center(domain1)
        #cmd.png("PNGsRenumb/%s_%s_CE.png"%(domain1, domain2), dpi = 300)
    except CmdException:
        pass

align_pairs = {}
with open("data/AllDataE1_v6_Numbered.txt", "r") as motif_pairs:
    for line in motif_pairs:
        line = line.strip().split(" ")
        if ("Dom1" not in line and len(line)>5):
            #print(line)
            domain1 = line[1]
            domain2 = line[2]
            residue1 = line[4]
            residue2 = line[5]
            
            residue1 = re.sub(",", "+", residue1)
            residue2 = re.sub(",", "+", residue2)
            
            #residue1 = re.sub(":", "-", residue1)
            #residue2 = re.sub(":", "-", residue2)
            
            align_pairs[int(line[0])] = [domain1, domain2, residue1, residue2]
            