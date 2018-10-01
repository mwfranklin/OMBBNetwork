from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2HDF.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 165-173 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 182-195 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 198-211 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 232-244 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 248-261 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 271-284 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 289-302 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 310-325 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 330-342 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 359-372 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 376-387 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 391-404 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 408-432 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 439-461 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 472-507 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 515-539 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 542-555 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 570-580 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("Astrand18", "resi 588-596 & chain A ")
cmd.color ("yellow", "Astrand18")


cmd.select("Astrand19", "resi 612-621 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 626-635 & chain A ")
cmd.color ("cyan", "Astrand20")


cmd.select("Astrand21", "resi 654-662 & chain A ")
cmd.color ("blue", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
