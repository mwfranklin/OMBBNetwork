from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/5T4Y.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Cstrand0", "resi 214-223 & chain C ")
cmd.color ("white", "Cstrand0")


cmd.select("Cstrand1", "resi 301-314 & chain C ")
cmd.color ("red", "Cstrand1")


cmd.select("Cstrand2", "resi 320-333 & chain C ")
cmd.color ("orange", "Cstrand2")


cmd.select("Cstrand3", "resi 337-353 & chain C ")
cmd.color ("purple", "Cstrand3")


cmd.select("Cstrand4", "resi 357-371 & chain C ")
cmd.color ("yellow", "Cstrand4")


cmd.select("Cstrand5", "resi 422-435 & chain C ")
cmd.color ("green", "Cstrand5")


cmd.select("Cstrand6", "resi 440-463 & chain C ")
cmd.color ("cyan", "Cstrand6")


cmd.select("Cstrand7", "resi 470-496 & chain C ")
cmd.color ("blue", "Cstrand7")


cmd.select("Cstrand8", "resi 502-525 & chain C ")
cmd.color ("purple", "Cstrand8")


cmd.select("Cstrand9", "resi 541-565 & chain C ")
cmd.color ("red", "Cstrand9")


cmd.select("Cstrand10", "resi 569-581 & chain C ")
cmd.color ("orange", "Cstrand10")


cmd.select("Cstrand11", "resi 590-601 & chain C ")
cmd.color ("yellow", "Cstrand11")


cmd.select("Cstrand12", "resi 616-640 & chain C ")
cmd.color ("green", "Cstrand12")


cmd.select("Cstrand13", "resi 674-699 & chain C ")
cmd.color ("cyan", "Cstrand13")


cmd.select("Cstrand14", "resi 703-722 & chain C ")
cmd.color ("blue", "Cstrand14")


cmd.select("Cstrand15", "resi 734-756 & chain C ")
cmd.color ("purple", "Cstrand15")


cmd.select("Cstrand16", "resi 760-777 & chain C ")
cmd.color ("red", "Cstrand16")


cmd.select("Cstrand17", "resi 858-867 & chain C ")
cmd.color ("orange", "Cstrand17")


cmd.select("Cstrand18", "resi 874-888 & chain C ")
cmd.color ("yellow", "Cstrand18")


cmd.select("Cstrand19", "resi 942-960 & chain C ")
cmd.color ("green", "Cstrand19")


cmd.select("Cstrand20", "resi 972-983 & chain C ")
cmd.color ("cyan", "Cstrand20")


cmd.select("Cstrand21", "resi 1007-1016 & chain C ")
cmd.color ("blue", "Cstrand21")


cmd.select("barrel", "Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
