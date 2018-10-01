from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2QTK.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10-23 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 34-50 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 55-68 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 92-102 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 107-111 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 133-139 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 146-153 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 178-186 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 192-203 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 205-217 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 223-235 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 244-256 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 261-272 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 298-311 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 318-332 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 340-351 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 361-372 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 377-390 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
