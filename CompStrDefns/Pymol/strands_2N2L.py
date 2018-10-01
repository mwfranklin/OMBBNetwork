from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2N2L.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4-15 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 24-37 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 41-52 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 67-81 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 84-99 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 110-124 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 130-139 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 145-156 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
