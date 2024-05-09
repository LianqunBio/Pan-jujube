f=open('filterd_all.final.genotype.map','r')
p=open('tem','w')

for eachline in f:
	eachline=eachline.strip()
	i=eachline.split()
	if i[0][0]=='0':
		p.write('%s\t%s\t%s\t%s\n' % (i[0][1],i[1],i[2],i[3]))
	else:
		p.write(eachline+'\n')
