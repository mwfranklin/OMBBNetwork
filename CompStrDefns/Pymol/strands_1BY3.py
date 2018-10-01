from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/1BY3.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 161-169 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 173-185 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 189-201 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 210-222 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 226-240 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 274-290 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 293-318 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 340-365 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 371-392 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 421-441 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 446-463 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 469-484 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 489-501 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 516-528 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 535-550 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 560-576 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 581-597 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 611-621 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("Astrand18", "resi 631-644 & chain A ")
cmd.color ("yellow", "Astrand18")


cmd.select("Astrand19", "resi 650-666 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 671-693 & chain A ")
cmd.color ("cyan", "Astrand20")


cmd.select("Astrand21", "resi 697-711 & chain A ")
cmd.color ("blue", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
