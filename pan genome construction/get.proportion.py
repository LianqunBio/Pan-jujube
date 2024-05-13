f=open('tem1','r') # sed 's/ //g' Orthogroups.tsv > tem1
p=open('perinfor','w')

dictp={}
dictd={}
dictc={}
lstcode=['Dong','S21','Z95','Z94','Z203','ZjujChr','KAH','ZspiChr']

for it in lstcode:
	dictc[it]=0
	dictd[it]=0
	dictp[it]=0

for eachline in f:
	eachline=eachline.strip()
	i=eachline.split('\t',1)
	if i[0]=='Orthogroup':
		continue
	else:
		outlst=i[1].split()
		if len(outlst)==8:
			for it in lstcode:
				value=i[1].count(it)
				dictc[it]+=value
		elif len(outlst)==1:
			for it in lstcode:
				if it in i[1]:
					value=i[1].count(it)
					dictp[it]+=value
				else:
					continue
		else:
			for it in lstcode:
				if it in i[1]:
					value=i[1].count(it)
					dictd[it]+=value
				else:
					continue
for it in lstcode:
	p.write('%s\t%d\t%d\t%d\n' % (it,dictc[it],dictd[it],dictp[it]))
