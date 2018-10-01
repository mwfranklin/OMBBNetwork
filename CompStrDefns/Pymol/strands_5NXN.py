from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/5NXN.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-22 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 35-49 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 55-64 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 76-86 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 90-99 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 130-140 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 145-158 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 172-184 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 187-197 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 223-233 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 238-252 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 257-271 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 278-289 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 298-312 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 315-326 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 343-351 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
