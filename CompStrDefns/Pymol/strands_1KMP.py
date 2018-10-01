from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/1KMP.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 224-232 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 242-254 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 257-270 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 278-290 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 294-308 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 332-347 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 351-369 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 375-395 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 401-422 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 435-456 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 461-478 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 484-501 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 504-516 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 535-547 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 552-563 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 581-594 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 603-616 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 630-643 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("Astrand18", "resi 646-660 & chain A ")
cmd.color ("yellow", "Astrand18")


cmd.select("Astrand19", "resi 678-691 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 697-717 & chain A ")
cmd.color ("cyan", "Astrand20")


cmd.select("Astrand21", "resi 724-740 & chain A ")
cmd.color ("blue", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
