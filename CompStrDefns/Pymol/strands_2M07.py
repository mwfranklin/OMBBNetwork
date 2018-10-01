from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2M07.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3-13 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 21-30 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 39-47 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 59-71 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 78-91 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 104-115 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 122-130 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 137-148 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
