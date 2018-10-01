from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/3WI5.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4-20 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 28-48 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 55-62 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 76-83 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 88-96 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 126-133 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 138-146 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 156-166 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 169-181 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 190-203 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 208-219 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 228-239 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 245-257 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 267-278 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 281-293 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 300-313 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
