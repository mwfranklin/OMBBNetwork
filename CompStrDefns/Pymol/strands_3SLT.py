from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/3SLT.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1039-1052 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 1056-1071 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 1077-1092 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 1097-1112 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 1118-1134 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 1140-1161 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 1164-1185 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 1192-1214 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 1220-1242 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 1248-1268 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 1271-1282 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 1289-1300 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
