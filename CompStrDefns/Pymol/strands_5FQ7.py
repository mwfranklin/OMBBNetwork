from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/5FQ7.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand0", "resi 178-185 & chain B ")
cmd.color ("white", "Bstrand0")


cmd.select("Bstrand1", "resi 253-261 & chain B ")
cmd.color ("red", "Bstrand1")


cmd.select("Bstrand2", "resi 267-280 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Bstrand3", "resi 288-302 & chain B ")
cmd.color ("purple", "Bstrand3")


cmd.select("Bstrand4", "resi 308-321 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 376-394 & chain B ")
cmd.color ("green", "Bstrand5")


cmd.select("Bstrand6", "resi 397-417 & chain B ")
cmd.color ("cyan", "Bstrand6")


cmd.select("Bstrand7", "resi 446-467 & chain B ")
cmd.color ("blue", "Bstrand7")


cmd.select("Bstrand8", "resi 473-494 & chain B ")
cmd.color ("purple", "Bstrand8")


cmd.select("Bstrand9", "resi 513-534 & chain B ")
cmd.color ("red", "Bstrand9")


cmd.select("Bstrand10", "resi 538-550 & chain B ")
cmd.color ("orange", "Bstrand10")


cmd.select("Bstrand11", "resi 557-568 & chain B ")
cmd.color ("yellow", "Bstrand11")


cmd.select("Bstrand12", "resi 583-610 & chain B ")
cmd.color ("green", "Bstrand12")


cmd.select("Bstrand13", "resi 628-656 & chain B ")
cmd.color ("cyan", "Bstrand13")


cmd.select("Bstrand14", "resi 660-679 & chain B ")
cmd.color ("blue", "Bstrand14")


cmd.select("Bstrand15", "resi 690-711 & chain B ")
cmd.color ("purple", "Bstrand15")


cmd.select("Bstrand16", "resi 718-730 & chain B ")
cmd.color ("red", "Bstrand16")


cmd.select("Bstrand17", "resi 801-810 & chain B ")
cmd.color ("orange", "Bstrand17")


cmd.select("Bstrand18", "resi 817-831 & chain B ")
cmd.color ("yellow", "Bstrand18")


cmd.select("Bstrand19", "resi 898-916 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 928-941 & chain B ")
cmd.color ("cyan", "Bstrand20")


cmd.select("Bstrand21", "resi 975-983 & chain B ")
cmd.color ("blue", "Bstrand21")


cmd.select("barrel", "Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
