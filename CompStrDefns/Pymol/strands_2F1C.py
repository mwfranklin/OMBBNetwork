from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2F1C.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 6-18 & chain X ")
cmd.color ("white", "Xstrand0")


cmd.select("Xstrand1", "resi 29-39 & chain X ")
cmd.color ("red", "Xstrand1")


cmd.select("Xstrand2", "resi 44-53 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 65-78 & chain X ")
cmd.color ("purple", "Xstrand3")


cmd.select("Xstrand4", "resi 84-97 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 107-122 & chain X ")
cmd.color ("green", "Xstrand5")


cmd.select("Xstrand6", "resi 125-138 & chain X ")
cmd.color ("cyan", "Xstrand6")


cmd.select("Xstrand7", "resi 148-161 & chain X ")
cmd.color ("blue", "Xstrand7")


cmd.select("Xstrand8", "resi 164-177 & chain X ")
cmd.color ("purple", "Xstrand8")


cmd.select("Xstrand9", "resi 188-200 & chain X ")
cmd.color ("red", "Xstrand9")


cmd.select("Xstrand10", "resi 203-217 & chain X ")
cmd.color ("orange", "Xstrand10")


cmd.select("Xstrand11", "resi 233-243 & chain X ")
cmd.color ("yellow", "Xstrand11")


cmd.select("Xstrand12", "resi 247-258 & chain X ")
cmd.color ("green", "Xstrand12")


cmd.select("Xstrand13", "resi 269-282 & chain X ")
cmd.color ("cyan", "Xstrand13")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
