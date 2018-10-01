from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/3QRC.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 31-41 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 48-63 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 67-82 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 89-107 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 110-129 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 132-150 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 154-164 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 171-181 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
