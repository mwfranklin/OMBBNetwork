from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/3PGR.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 44-59 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 70-88 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 92-108 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 115-136 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 140-158 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 197-217 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 221-233 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 269-283 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 287-296 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 324-333 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 340-349 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 366-377 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 380-397 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 404-420 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
