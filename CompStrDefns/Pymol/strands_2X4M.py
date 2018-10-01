from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2X4M.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 12-32 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 40-60 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 66-86 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 96-121 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 125-150 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 154-184 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 189-208 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 213-235 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 238-259 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 268-292 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
