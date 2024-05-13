f=open('kaks.path','r')
p=open('kaks.result.xls','w')

for eachline in f:
	eachline=eachline.strip()
	groupID=eachline.split('/')[-2]
	newfile=open(eachline,'r')
	for line in newfile:
		line=line.strip()
		i=line.split()
		if i[0]=='Sequence':
			continue
		else:
			nameID=i[0]
			value=i[4]
			if value=='NA':
				continue
			else:
				p.write(groupID+'\t'+nameID+'\t'+value+'\n')

