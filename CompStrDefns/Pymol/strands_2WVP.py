from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2WVP.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6-18 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 29-39 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 44-53 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 65-78 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 84-97 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 107-122 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 126-138 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 148-161 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 164-177 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 188-200 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 203-217 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 233-243 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 247-258 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 269-282 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
