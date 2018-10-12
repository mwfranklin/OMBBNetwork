from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitHubProjects/v6_2018_Network/CompStrDefns/CompPDBs/3T20.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-21 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 31-47 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 52-65 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 87-99 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 104-108 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 130-136 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 143-150 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 179-189 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 192-203 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 205-217 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 223-235 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 244-256 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 259-273 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 299-310 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 315-332 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 337-351 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 361-372 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 377-391 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
