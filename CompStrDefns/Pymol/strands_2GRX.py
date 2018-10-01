from pymol import cmd, stored
cmd.load("/Users/meghan/Documents/PhD/GitProjects/v6_2018_Network/CompStrDefns/CompPDBs/2GRX.pdb")
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 161-169 & chain A ")
cmd.color ("white", "Astrand0")


cmd.select("Astrand1", "resi 173-182 & chain A ")
cmd.color ("red", "Astrand1")


cmd.select("Astrand2", "resi 191-203 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 208-221 & chain A ")
cmd.color ("purple", "Astrand3")


cmd.select("Astrand4", "resi 226-240 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 274-289 & chain A ")
cmd.color ("green", "Astrand5")


cmd.select("Astrand6", "resi 295-318 & chain A ")
cmd.color ("cyan", "Astrand6")


cmd.select("Astrand7", "resi 340-365 & chain A ")
cmd.color ("blue", "Astrand7")


cmd.select("Astrand8", "resi 371-393 & chain A ")
cmd.color ("purple", "Astrand8")


cmd.select("Astrand9", "resi 430-452 & chain A ")
cmd.color ("red", "Astrand9")


cmd.select("Astrand10", "resi 457-474 & chain A ")
cmd.color ("orange", "Astrand10")


cmd.select("Astrand11", "resi 480-494 & chain A ")
cmd.color ("yellow", "Astrand11")


cmd.select("Astrand12", "resi 502-512 & chain A ")
cmd.color ("green", "Astrand12")


cmd.select("Astrand13", "resi 527-538 & chain A ")
cmd.color ("cyan", "Astrand13")


cmd.select("Astrand14", "resi 546-561 & chain A ")
cmd.color ("blue", "Astrand14")


cmd.select("Astrand15", "resi 571-587 & chain A ")
cmd.color ("purple", "Astrand15")


cmd.select("Astrand16", "resi 592-608 & chain A ")
cmd.color ("red", "Astrand16")


cmd.select("Astrand17", "resi 622-633 & chain A ")
cmd.color ("orange", "Astrand17")


cmd.select("Astrand18", "resi 640-655 & chain A ")
cmd.color ("yellow", "Astrand18")


cmd.select("Astrand19", "resi 661-677 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 682-704 & chain A ")
cmd.color ("cyan", "Astrand20")


cmd.select("Astrand21", "resi 708-722 & chain A ")
cmd.color ("blue", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
