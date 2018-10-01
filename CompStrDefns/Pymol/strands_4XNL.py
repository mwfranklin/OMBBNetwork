from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/4XNL.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 43-54 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 66-79 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 85-96 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 123-135 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 145-150 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 166-172 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 178-185 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 205-215 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 219-229 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 249-261 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 273-291 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 301-318 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 323-334 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 377-388 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 391-402 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 426-437 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 457-466 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 479-490 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
