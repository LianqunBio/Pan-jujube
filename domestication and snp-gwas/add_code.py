f=open('sweep_regine','r')
p=open('code_sweep_regine','w')
p2=open('sweep-regine-info.xls','w')
a=0
for eachline in f:
	eachline = eachline.strip()
	i = eachline.split()
	if i[0][0]=='#':
		pass
	else:
		a+=1
		p.write('DS-P%03d-%s\n' % (a,eachline))
		p2.write('DS-P%03d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (a,i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

