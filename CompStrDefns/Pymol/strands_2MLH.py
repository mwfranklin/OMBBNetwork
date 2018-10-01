from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2MLH.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-15 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 56-61 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 66-71 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 117-123 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 132-141 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 191-202 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 204-216 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 231-237 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
