from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/5O68.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 108-119 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 146-160 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 164-178 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 197-215 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 223-232 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 266-275 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 281-296 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 309-327 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 331-348 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 355-373 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 378-389 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 397-406 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
