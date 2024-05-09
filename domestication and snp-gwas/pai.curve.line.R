pdf("pai.curve.line.pdf",width=70,height=10)


par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr01.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr01 (Mb)"), cex=2)
read.table("chr01.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}



par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr02.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr02 (Mb)"), cex=2)
read.table("chr02.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}



par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr03.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr03 (Mb)"), cex=2)
read.table("chr03.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}


par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr04.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr04 (Mb)"), cex=2)
read.table("chr04.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}

par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr05.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr05 (Mb)"), cex=2)
read.table("chr05.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}


par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr06.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr06 (Mb)"), cex=2)
read.table("chr06.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}

par(mgp=c(2,1,0),mfrow=c(1,1))
plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr07.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr07 (Mb)"), cex=2)
read.table("chr07.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
		lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}


par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr08.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr08 (Mb)"), cex=2)
read.table("chr08.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}


par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr09.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr09 (Mb)"), cex=2)
read.table("chr09.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}



par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr10.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr10 (Mb)"), cex=2)
read.table("chr10.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}


par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr11.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr11 (Mb)"), cex=2)
read.table("chr11.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}



par(mgp=c(2,1,0),mfrow=c(1,1))

plot(c(0,0)~c(0,0),col="white",xlim=c(-1,90),axes=F,xlab="",ylim=c(-30,10),ylab="Pai*(10-3)",cex.lab=3,lwd=10,cex.lab=3) 
read.table("chr12.raw.poly")->da
da$V2/1000000->pos
da$V5*1000->pi_zp
lines(pos,pi_zp,lwd=1.5,col="orange")
da$V4*1000->pi_ys
lines(pos,pi_ys,lwd=1.5,col="forestgreen")
axis(side=1, at=seq(0,90,2), labels=seq(0,90,2), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
axis(side=2, at=c(0,2,4,6,8,10), labels=c(0,2,4,6,8,10), pos=0, cex.axis=2, cex.lab=5, tck=-0.02)
legend(-4,8,c("Candolleanum","Landrace"),lty=1,col=c("forestgreen","orange"),lwd=1.5,cex=1)
text(-4,-0.8, adj=0, labels=paste("chr12 (Mb)"), cex=2)
read.table("chr12.sweep.regine")->sweep
sweep$V2/1000000->chr_s
sweep$V3/1000000->chr_e
for (i in 1:length(chr_e)) {
	lines(c(9,9)~c(chr_s[i],chr_e[i]),lwd=1.5,col="blue")
}



