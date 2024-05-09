library(qqman)
#pdf("qqman_EMMAX.pdf", width=20,height=10)
png(file="qqman_EMMAX.png", bg="white", width=3000, height=500)
layout(mat = matrix(c(1,2),nrow = 1,ncol = 2),heights = 400,widths = c(2500, 500))

data<-read.table("input",head=T)
manhattan(data, chr="CHR", bp="BP", p="P", snp="SNP", col=c("forestgreen","orange2"), chrlabs=c(1:12), suggestiveline=FALSE, genomewideline=-log10(2.41E-56), logp=TRUE, main='Manhattan Plot',cex=3.5,cex.axis=2, cex.lab=2, cex.main=2 )
qq(data$P, col='blue4', main='QQplot', cex.axis=2, cex.lab=2, cex.main=2)
dev.off()
