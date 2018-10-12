from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitHubProjects/v6_2018_Network/CompStrDefns/CompPDBs/3K1B.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10-22 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 36-49 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 56-65 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 80-90 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 94-103 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 133-143 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 148-165 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 169-181 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 186-196 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 209-220 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 224-242 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 246-264 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 268-281 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 289-302 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 306-317 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 331-339 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
