from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitHubProjects/v6_2018_Network/CompStrDefns/CompPDBs/5MWV.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-14 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 34-40 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 45-51 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 68-78 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 86-96 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 108-122 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 128-137 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 151-160 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 168-174 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 194-200 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 207-211 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 237-245 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 249-257 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 274-281 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
