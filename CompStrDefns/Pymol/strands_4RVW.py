from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/4RVW.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 149-157 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 162-171 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 178-188 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 207-217 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 224-238 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 301-317 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 325-343 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 348-362 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 370-385 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 397-413 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 417-432 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 458-471 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 475-484 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 517-526 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 532-549 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 570-587 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 592-606 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 630-647 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("Astrand18", "resi 653-664 & chain A ")
cmd.color ("yellow", "Astrand18")


cmd.select("Astrand19", "resi 674-688 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 694-703 & chain A ")
cmd.color ("cyan", "Astrand20")


cmd.select("Astrand21", "resi 725-733 & chain A ")
cmd.color ("blue", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
