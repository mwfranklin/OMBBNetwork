from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/5O67.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 108-119 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 144-160 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 164-180 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 195-214 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 223-231 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 266-275 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 281-299 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 307-327 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 331-350 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 355-373 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 378-387 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 397-406 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
