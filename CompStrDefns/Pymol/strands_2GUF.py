from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2GUF.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 137-145 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 149-160 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 164-175 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 197-208 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 213-227 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 242-257 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 262-277 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 289-304 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 308-323 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 333-347 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 352-363 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 368-377 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 382-394 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 413-425 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 430-447 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 451-470 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 476-487 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 497-509 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("Astrand18", "resi 515-528 & chain A ")
cmd.color ("yellow", "Astrand18")


cmd.select("Astrand19", "resi 539-555 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 559-567 & chain A ")
cmd.color ("cyan", "Astrand20")


cmd.select("Astrand21", "resi 585-591 & chain A ")
cmd.color ("blue", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
