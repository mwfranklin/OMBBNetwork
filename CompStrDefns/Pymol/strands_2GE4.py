from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2GE4.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6-16 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 34-45 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 49-55 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 75-85 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 90-103 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 118-130 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 136-142 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 161-170 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
