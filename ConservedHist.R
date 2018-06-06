setwd("/Users/meghan/Documents/PhD/GitHubProjects/v6_2018_Network/")

cons_values <- c("25", "50", "85")
for (x in seq_along(cons_values)){
  print(cons_values[x])
  cons_IDs <- as.matrix(feather::read_feather(paste0("data/ConsStrandIDs", cons_values[x], ".feather")))
  strand_sizes <- c("8", "10", "12", "14", "16", "18", "22")
  rownames(cons_IDs) <- strand_sizes
  colnames(cons_IDs) <- seq(1,22,1)
  cons_IDs["8", 1:8]
  max_values <- apply(cons_IDs, MAR = 1, FUN = max)
  print(max_values)
  if (cons_values[x] == "25"){
    max_values <- c(180, 15, 90, 120, 130, 30, 250) #for 25%
  }else if (cons_values[x] == "50"){
    max_values <- c(300, 20, 130, 140, 300, 325, 500) #for 50%
  }else{
    max_values <- c(450, 40, 175, 175, 600, 600, 600) #for 85%
  }
  
  tiff(paste0("NetworkGraphs/ConsID_", cons_values[x], ".tiff"), width = 9, height = 5, units = "in", res = 300)
  par(mfrow = c(2,4), oma = c(1, 2, 3, 2), mgp=c(2.5,1,0), mar = c(4, 4, 2, 1), xpd = T, cex.axis = 1.4, cex.lab = 1.7)
  for (value in seq_len(nrow(cons_IDs))){
    #print(value)
    mp <- barplot(cons_IDs[value,1:strand_sizes[value]], ylim = c(0,max_values[value]), main = paste0(strand_sizes[value], "-Stranded Barrels"), xlab = "Strand ID", ylab = "Counts", cex.main = 1.6)
    #axis(side=2, pos=-0.2)
    axis(side=1, at =mp, labels = F)
  }
  mtext("Conserved Strand Identity", outer = T, cex = 1.8)
  dev.off()
}

#for length of alignments
for (x in seq_along(cons_values)){
  print(cons_values[x])
  cons_lengths <- as.matrix(feather::read_feather(paste0("data/ConsLengths", cons_values[x], ".feather")))
  strand_sizes <- c("8", "10", "12", "14", "16", "18", "22")
  rownames(cons_lengths) <- strand_sizes
  colnames(cons_lengths) <- seq(1,22,1)
  cons_lengths["8", 1:8]
  max_values <- apply(cons_lengths, MAR = 1, FUN = max)
  print(max_values)
  if (cons_values[x] == "25"){
    max_values <- c(60, 10, 20, 20, 60, 20, 180) #for 25%
  }else if (cons_values[x] == "50"){
    max_values <- c(100, 10, 30, 40, 120, 250, 350) #for 50%
  }else{
    max_values <- c(150, 20, 40, 40, 250, 450, 500) #for 85%
  }
  
  tiff(paste0("NetworkGraphs/ConsLength_", cons_values[x], ".tiff"), width = 9, height = 5, units = "in", res = 300)
  par(mfrow = c(2,4), oma = c(1, 2, 3, 2), mgp=c(2.5,1,0), mar = c(4, 4, 2, 1), xpd = T, cex.axis = 1.4, cex.lab = 1.7)
  for (value in seq_len(nrow(cons_IDs))){
    #print(value)
    mp <- barplot(cons_lengths[value,1:strand_sizes[value]], ylim = c(0,max_values[value]), main = paste0(strand_sizes[value], "-Stranded Barrels"), xlab = "Length of Alignment", ylab = "Counts")
    #axis(side=2, pos=-0.2)
    axis(side=1, at =mp, labels = F)
  }
  mtext("Conserved Strand Identity", outer = T, cex = 1.8)
  dev.off()
}
