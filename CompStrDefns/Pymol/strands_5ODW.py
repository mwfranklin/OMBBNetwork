from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/5ODW.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 278-286 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 288-299 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 307-319 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 326-340 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 343-358 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 390-405 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 411-436 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 440-465 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 472-498 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 519-539 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 543-557 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 563-579 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 582-594 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 611-624 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 629-647 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 662-681 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 684-699 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 706-720 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("Astrand18", "resi 729-746 & chain A ")
cmd.color ("yellow", "Astrand18")


cmd.select("Astrand19", "resi 751-771 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 775-792 & chain A ")
cmd.color ("cyan", "Astrand20")


cmd.select("Astrand21", "resi 800-812 & chain A ")
cmd.color ("blue", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
