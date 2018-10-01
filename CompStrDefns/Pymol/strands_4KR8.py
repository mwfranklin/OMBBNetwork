from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/4KR8.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 12-23 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 32-45 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 52-63 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 75-85 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 89-95 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 131-141 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 146-159 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 169-180 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 185-193 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 209-218 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 222-240 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 245-263 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 267-279 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 288-302 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 306-314 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 332-341 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
