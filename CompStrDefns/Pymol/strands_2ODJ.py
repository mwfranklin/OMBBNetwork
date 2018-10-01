from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2ODJ.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 17-31 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 39-55 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 60-76 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 97-107 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 113-116 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 138-144 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 151-172 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 181-193 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 196-207 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 209-223 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 227-241 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 251-261 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 266-275 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 311-322 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 333-346 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 362-376 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 387-400 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 406-422 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
