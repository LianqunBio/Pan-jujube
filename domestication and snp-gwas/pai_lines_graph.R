pdf("pai_lines.pdf", width=20,height=5)
par(mgp=c(0,0.5,0))
plot(c(0,0)~c(0,0),col="white",xlim=c(0,731.287687),axes=F,xlab="",ylim=c(0,5),ylab="pai_wild/pai_cul",main="Domestication",cex.lab=2,cex.main=2)# adjugement the ylim

db<-read.table("graph.input")
rition_value<-db$V3
pos<-db$V2/1000000
Chr_ID<-db$V1
for (i in 1:length(rition_value)) {
if (Chr_ID[i]=='chr01'){
if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i],pos[i]),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i],pos[i]),lty=1,col="darkgoldenrod1",lwd=1);
}

} else if (Chr_ID[i]=='chr02'){
if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i]+88.591686,pos[i]+88.591686),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i]+88.591686,pos[i]+88.591686),lty=1,col="darkgoldenrod1",lwd=1);
}
} else if (Chr_ID[i]=='chr03'){
if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i]+134.694601,pos[i]+134.694601),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i]+134.694601,pos[i]+134.694601),lty=1,col="darkgoldenrod1",lwd=1);
}
} else if (Chr_ID[i]=='chr04'){
if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i]+195.402171,pos[i]+195.402171),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i]+195.402171,pos[i]+195.402171),lty=1,col="darkgoldenrod1",lwd=1);
}
} else if (Chr_ID[i]=='chr05'){
if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i]+264.638502,pos[i]+264.638502),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i]+264.638502,pos[i]+264.638502),lty=1,col="darkgoldenrod1",lwd=1);
}
} else if (Chr_ID[i]=='chr06'){
if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i]+320.238199,pos[i]+320.238199),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i]+320.238199,pos[i]+320.238199),lty=1,col="darkgoldenrod1",lwd=1);
}
} else if (Chr_ID[i]=='chr07'){
	if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i]+379.329777,pos[i]+379.329777),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i]+379.329777,pos[i]+379.329777),lty=1,col="darkgoldenrod1",lwd=1);
}
} else if (Chr_ID[i]=='chr08'){
	if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i]+436.969094,pos[i]+436.969094),lty=1,col="dodgerblue2",lwd=1);
} else  {
	lines(c(0,rition_value[i])~c(pos[i]+436.969094,pos[i]+436.969094),lty=1,col="darkgoldenrod1",lwd=1);
}
} else if (Chr_ID[i]=='chr09'){
	if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i]+496.195094,pos[i]+496.195094),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i]+496.195094,pos[i]+496.195094),lty=1,col="darkgoldenrod1",lwd=1);
}
} else if (Chr_ID[i]=='chr10'){
	if(rition_value[i]<0) {	
	lines(c(0,rition_value[i])~c(pos[i]+563.795394,pos[i]+563.795394),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i]+563.795394,pos[i]+563.795394),lty=1,col="darkgoldenrod1",lwd=1);
}
} else if (Chr_ID[i]=='chr11'){
	if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i]+624.839545,pos[i]+624.839545),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i]+624.839545,pos[i]+624.839545),lty=1,col="darkgoldenrod1",lwd=1);
}
} else if (Chr_ID[i]=='chr12'){
	if(rition_value[i]<0) {
	lines(c(0,rition_value[i])~c(pos[i]+671.616932,pos[i]+671.616932),lty=1,col="dodgerblue2",lwd=1);
} else {
	lines(c(0,rition_value[i])~c(pos[i]+671.616932,pos[i]+671.616932),lty=1,col="darkgoldenrod1",lwd=1);
}
}
}


lines(c(1.706683,1.706683)~c(0,731.287687),lty=5,lwd=2,col="black")


lines(c(0,0.5)~c(88.591686,88.591686),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(134.694601,134.694601),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(195.402171,195.402171),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(264.638502,264.638502),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(320.238199,320.238199),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(379.329777,379.329777),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(436.969094,436.969094),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(496.195094,496.195094),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(563.795394,563.795394),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(624.839545,624.839545),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(671.616932,671.616932),lty=5,lwd=2,col="black")
lines(c(0,0.5)~c(731.287687,731.287687),lty=5,lwd=2,col="black")




axis(side=1,at=c(0,44.33,112.97,168.42,235.67,297.81,353.61,411.76,468.61,527.85,588.45,641.11,694.43,725.017384),labels=c("","1","2","3","4","5","6","7","8","9","10","11","12",""),pos=0,lwd=1, tck=0,cex=2)
axis(side=2,at=seq(0,5,1),labels=seq(0,5,1),pos=0,las=1,lwd=1, tck=0,tck=-0.01,cex=2)
#text(766.0189215,-2,labels="Chromosome",cex=2)
dev.off()

