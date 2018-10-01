from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/1G90.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6-18 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 30-45 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 49-58 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 73-85 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 91-104 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 116-131 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 135-142 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 161-168 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
