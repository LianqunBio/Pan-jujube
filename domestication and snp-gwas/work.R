library(qvalue)
rawin <- read.table("inputfile.txt", header = F, sep="\t")
sigvalues <- rawin$V4
FDRvalues<-qvalue( p= sigvalues)
outinfor<-FDRvalues$qvalues
write.table(outinfor, file = "output.txt", sep = "\t", row.names = FALSE)
