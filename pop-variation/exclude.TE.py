import gzip
f1=open('Z95.fa.mod.EDTA.TEanno.gff3','r')
f2=gzip.open('all.snp.vcf.gz','rt')
p=open('TE.excluded.snp.vcf','w')

dict1={}

for eachline in f1:
	eachline=eachline.strip()
	i=eachline.split()
	if eachline[0]=='#':
		continue
	else:
		chrID=i[0]
		start=int(i[3])
		end=int(i[4])+1
		for it in range(start,end):
			ID=chrID+'\t'+str(it)
			if (ID not in dict1) and (i[0]!='z95_chr00'):
				print(ID)
				dict1[ID]=0
			else:
				continue

for eachline in f2:
	eachline=eachline.strip()
	i=eachline.split()
#	print(eachline)
	if eachline[0]=='#':
		continue
	else:
		ID=i[0]+'\t'+i[1]
		if ID not in dict1:
			p.write(eachline+'\n')
		else:
			continue



