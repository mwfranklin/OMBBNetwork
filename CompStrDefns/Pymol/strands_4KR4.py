from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/4KR4.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 14-23 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 32-47 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 51-61 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 75-85 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 89-95 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 131-142 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 146-159 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 170-179 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 186-194 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 209-218 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 224-240 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 245-261 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 268-281 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 286-299 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 305-316 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 332-341 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
