from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/6EHF.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10-23 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 30-46 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 50-59 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 67-76 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 81-86 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 120-126 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 132-140 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 145-155 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 159-179 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 186-204 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 209-220 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 227-241 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 244-259 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 264-277 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 280-292 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 311-325 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
