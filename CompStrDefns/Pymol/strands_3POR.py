from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitHubProjects/v6_2018_Network/CompStrDefns/CompPDBs/3POR.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3-14 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 20-33 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 40-52 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 58-64 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 69-72 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 119-123 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 127-137 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 146-157 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 160-174 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 178-191 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 194-208 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 225-239 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 244-254 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 258-271 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 274-285 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 292-301 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
