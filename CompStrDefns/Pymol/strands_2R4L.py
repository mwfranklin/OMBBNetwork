from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2R4L.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 44-62 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 66-88 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 91-107 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 120-135 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 139-157 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 197-216 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 222-241 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 259-281 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 288-307 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 314-333 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 338-351 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 366-376 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 380-397 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 404-420 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
