from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2N6L.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-13 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 46-53 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 56-63 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 93-99 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 109-116 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 147-154 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 161-166 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 200-207 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
