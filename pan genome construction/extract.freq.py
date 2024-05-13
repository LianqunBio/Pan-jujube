f=open('Orthogroups.GeneCount.tsv','r')
p=open('freq.out.xls','w')

dict1={}

for it in range(1,9):
	dict1[it]=0

for eachline in f:
	eachline=eachline.strip()
	print(eachline)
	i=eachline.split()
	if i[0]=='Orthogroup':
		continue
	else:
		num=0
		for it in i:
			if it==i[0]:
				continue
			else:
				if it!='0':
					num+=1
				else:
					continue
		dict1[num-1]+=1

for it in range(1,9):
	p.write('%sd\t%d\n' % (it,dict1[it]))

