f=open('genotypes.vcf','r')
p1=open('name.list','w')
p2=open('sv.genotype','w')

for eachline in f:
	eachline=eachline.strip()
	i=eachline.split()
	if eachline[0]=='#':
		if i[0]=='#CHROM':
			codelst=eachline.split('\t',9)[9].split()
			for it in codelst:
				p1.write(it+'\n')
		else:
			continue
	else:
		chrID=i[0]
		pos=i[1]
		codelst=eachline.split('\t',9)[9].split()
		strout=''
		for it in codelst:
			infor=it.split(':')[0]
			if infor=='.':
				strout+='-'+' '
			elif infor=='0/0' or infor=='0|0':
				strout+='A'+' '
			elif infor=='1/1' or infor=='1|1':
				strout+='C'+' '
			elif infor=='0/1' or infor=='0|1':
				strout+='M'+' '
			else:
				print(infor)
		p2.write('%s\t%s\t%s\n' % (chrID,pos,strout))
