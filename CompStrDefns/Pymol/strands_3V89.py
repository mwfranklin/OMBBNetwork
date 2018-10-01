from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/3V89.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 187-197 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 200-212 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 218-249 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 281-318 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 327-379 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 391-416 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 424-445 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 464-486 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 497-527 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 548-592 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 595-610 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 620-633 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 639-649 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 673-684 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 690-711 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 718-742 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 756-770 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 789-797 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("Astrand18", "resi 805-825 & chain A ")
cmd.color ("yellow", "Astrand18")


cmd.select("Astrand19", "resi 833-854 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 861-874 & chain A ")
cmd.color ("cyan", "Astrand20")


cmd.select("Astrand21", "resi 902-912 & chain A ")
cmd.color ("blue", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
