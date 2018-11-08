from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitHubProjects/v6_2018_Network/CompStrDefns/CompPDBs/1UYO.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 821-829 & chain X ")
cmd.color ("white", "Xstrand0")


cmd.select("Xstrand1", "resi 840-852 & chain X ")
cmd.color ("red", "Xstrand1")


cmd.select("Xstrand2", "resi 859-872 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 877-893 & chain X ")
cmd.color ("purple", "Xstrand3")


cmd.select("Xstrand4", "resi 897-916 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 920-941 & chain X ")
cmd.color ("green", "Xstrand5")


cmd.select("Xstrand6", "resi 948-968 & chain X ")
cmd.color ("cyan", "Xstrand6")


cmd.select("Xstrand7", "resi 974-996 & chain X ")
cmd.color ("blue", "Xstrand7")


cmd.select("Xstrand8", "resi 999-1009 & chain X ")
cmd.color ("purple", "Xstrand8")


cmd.select("Xstrand9", "resi 1042-1052 & chain X ")
cmd.color ("red", "Xstrand9")


cmd.select("Xstrand10", "resi 1058-1067 & chain X ")
cmd.color ("orange", "Xstrand10")


cmd.select("Xstrand11", "resi 1073-1082 & chain X ")
cmd.color ("yellow", "Xstrand11")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
