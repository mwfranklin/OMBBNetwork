setwd("/Volumes/G_Drive/StructureAlign/NirBenTal/Joanna_and_Meghan/v6_2018")

read_and_convert <- function(filename){
  new_matrix <- as.matrix(feather::read_feather(filename))
  row.names(new_matrix) <- seq(0,26)
  new_matrix <- new_matrix[c("8", "10", "12", "14", "16", "18", "22"), c("8", "10", "12", "14", "16", "18", "22")]
  #print(new_matrix)
  return(new_matrix)
}

barrel_nonbarrel <- function(prepped_matrix){
  barrel_nonbarrel_counts <- matrix(NA, nrow = nrow(prepped_matrix), ncol = 2)
  for (x in seq_len(nrow(prepped_matrix))){
    barrel_nonbarrel_counts[x,2] <- sum(prepped_matrix[x,]) - prepped_matrix[x,x] 
    barrel_nonbarrel_counts[x,1] <- prepped_matrix[x,x] 
  }
  #print(barrel_nonbarrel_counts)
  colnames(barrel_nonbarrel_counts) <- c("Same", "Different")
  rownames(barrel_nonbarrel_counts) <- rownames(prepped_matrix)
  return(barrel_nonbarrel_counts)
}

barrel_diffbarrel_counts <- function(prepped_matrix){
  #calculate the possible connections btween barrels of same/diff size
  all_seqIDs <- list()
  #print(prepped_matrix)
  for (seqID in seq_len(ncol(prepped_matrix))){
    barrel_nonbarrel_counts <- matrix(NA, nrow = nrow(prepped_matrix), ncol = 2)
    for (x in seq_len(nrow(prepped_matrix))){
      barrel_nonbarrel_counts[x,2] <- sum(prepped_matrix[,seqID]) - prepped_matrix[x,seqID] 
      barrel_nonbarrel_counts[x,1] <- prepped_matrix[x,seqID] 
    }
    colnames(barrel_nonbarrel_counts) <- c("Same", "Different")
    rownames(barrel_nonbarrel_counts) <- rownames(prepped_matrix)
    all_seqIDs[[colnames(prepped_matrix)[seqID]]] <- barrel_nonbarrel_counts
  }
  #print(all_seqIDs)
  return(all_seqIDs)
}

calc_probabilities <- function(prepped_matrix){
  probabilities <- matrix(NA, nrow = nrow(prepped_matrix), ncol = 2)
  for (x in seq_len(nrow(prepped_matrix))){
    probabilities[x,1] <- prepped_matrix[x,1]*(prepped_matrix[x,1]-1)                  
    probabilities[x,2] <- prepped_matrix[x,1]*prepped_matrix[x,2]
  }
  colnames(probabilities) <- c("Same", "Different")
  rownames(probabilities) <- rownames(prepped_matrix)
  return(probabilities)
}

convert_to_vect<- function(prepped_matrix){
  prepped_matrix[prepped_matrix == 0] <- NA
  prepped_vect <- as.vector(t(prepped_matrix))
  names(prepped_vect) <- c(paste0(rep( c(seq(8,18,2), 22), each = 7), "+",rep( c(seq(8,18,2), 22), times = 7) ))
  prepped_vect <- prepped_vect[! is.na(prepped_vect)]
  return(prepped_vect)
}

prep_for_kable <- function(prepped_matrix){
  #sets 0 to NA and removes bottom diagonal matrix 
  prepped_matrix[prepped_matrix == 0] <- NA
  for (x in seq_len(nrow(prepped_matrix))){
    for (y in seq_len(nrow(prepped_matrix))){
      if (y < x){
        prepped_matrix[x, y] <- NA
      }
    }
  }
  min_int <- as.matrix(apply(prepped_matrix, MARGIN = 1, FUN = min, na.rm = T))
  test_interaction <- ifelse(prepped_matrix<0.001, formatC(prepped_matrix, format = "e", digits = 2), round(prepped_matrix, digits = 3))
  for (x in seq_len(nrow(prepped_matrix))){
    #print(min_int[x])
    test_interaction[x,which(prepped_matrix[x,] == min_int[x])] <- cell_spec(test_interaction[x,which(prepped_matrix[x,] == min_int[x])], bold = T, format='latex')
  }
  test_interaction[which(is.na(prepped_matrix))] <- cell_spec(prepped_matrix[which(is.na(prepped_matrix))], color = "white", format='latex')
  return(test_interaction)
}

read_and_make_graph <- function(value, probabilities, loc_to_save){
  e_value_1 <- read_and_convert(paste0("data/BtwnBarrels/BtwnBarrelEVals2_", value,".feather"))
  e_value_1_BNB <- barrel_nonbarrel(e_value_1)/probabilities
  e_value_3 <- read_and_convert(paste0("data/BtwnBarrels/BtwnBarrelEVals4_", value,".feather"))
  e_value_3_BNB <- barrel_nonbarrel(e_value_3)/probabilities
  e_value_5 <- read_and_convert(paste0("data/BtwnBarrels/BtwnBarrelEVals6_", value,".feather"))
  e_value_5_BNB <- barrel_nonbarrel(e_value_5)/probabilities
  
  tiff(paste0(loc_to_save, "/MinEValues_", value, ".tiff"), width = 10, height = 8, units = "in", res=300)
  par(mfrow = c(1,3), oma = c(2, 0, 2, 0))
  barplot(t(e_value_1_BNB), beside = T, main = expression("E-values <" ~ 10^{-2}), ylab = "Probability of alignment", xlab = "Strands per Barrel", ylim = c(0,1) )
  barplot(t(e_value_3_BNB), beside = T, main = expression("E-values <" ~ 10^{-4}), ylab = "Probability of alignment", xlab = "Strands per Barrel", ylim = c(0,1) )
  barplot(t(e_value_5_BNB), beside = T, main = expression("E-values <" ~ 10^{-6}), ylab = "Probability of alignment", xlab = "Strands per Barrel", ylim = c(0,1) )
  plot(0, type = "n", axes=FALSE, ann = FALSE)
  legend("topleft", legend = c("Same Size", "Different Size"), fill = gray.colors(2), cex = 1.5)
  mtext(bquote(SeqID >= .(value)*'%'), outer = T, cex = 1.5)
  box(which = "outer")
  dev.off()
}

barrel_lengths <- read.delim("data/BtwnBarrels/ProtoLengths.txt", sep = "\t", header = F, row.names = 1)
colnames(barrel_lengths) <- seq(0,26)
barrel_lengths <- t(barrel_lengths[,c("8", "10", "12", "14", "16", "18", "22")])
barrel_prob <- barrel_diffbarrel_counts(barrel_lengths)
barrel_prob <- lapply(barrel_prob, FUN = calc_probabilities)

e_value_1 <- read_and_convert(paste0("BtwnBarrelEVals1_", 25,".feather"))
e_value_1_BNB <- barrel_nonbarrel(e_value_1)#/probabilities

read_and_make_graph("85", barrel_prob[["85%"]], "NetworkGraphs")
read_and_make_graph("50", barrel_prob[["50%"]])
read_and_make_graph("25", barrel_prob[["25%"]])