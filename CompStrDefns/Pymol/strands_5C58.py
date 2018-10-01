from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/5C58.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 242-252 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 256-267 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 270-282 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 322-335 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 338-354 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 375-391 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 396-414 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 427-445 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 452-471 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 482-497 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 500-524 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 548-572 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 577-600 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 608-630 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 639-658 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 675-695 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 700-716 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 749-775 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("Astrand18", "resi 779-789 & chain A ")
cmd.color ("yellow", "Astrand18")


cmd.select("Astrand19", "resi 810-821 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 824-839 & chain A ")
cmd.color ("cyan", "Astrand20")


cmd.select("Astrand21", "resi 852-864 & chain A ")
cmd.color ("blue", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
