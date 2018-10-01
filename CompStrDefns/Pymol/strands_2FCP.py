from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2FCP.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 161-169 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 171-184 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 189-203 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 208-222 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 228-240 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 274-290 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 294-318 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 340-365 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 372-393 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 428-449 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 455-471 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 476-492 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 500-510 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 525-536 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 542-559 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 569-586 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 590-606 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 620-630 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("Astrand18", "resi 640-653 & chain A ")
cmd.color ("yellow", "Astrand18")


cmd.select("Astrand19", "resi 659-673 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 684-702 & chain A ")
cmd.color ("cyan", "Astrand20")


cmd.select("Astrand21", "resi 706-720 & chain A ")
cmd.color ("blue", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
