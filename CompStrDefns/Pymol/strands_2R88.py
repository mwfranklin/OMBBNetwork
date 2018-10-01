from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2R88.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 44-59 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 70-88 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 92-107 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 114-133 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 140-157 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 196-216 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 220-232 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 268-280 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 287-296 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 323-332 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 337-348 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 365-376 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 379-396 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 403-419 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
