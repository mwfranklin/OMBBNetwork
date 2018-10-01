from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/3BRZ.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 44-58 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 81-88 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 94-110 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 128-143 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 150-168 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 199-229 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 232-257 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 264-288 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 294-316 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 322-342 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 349-358 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 377-384 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 391-404 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 418-433 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
