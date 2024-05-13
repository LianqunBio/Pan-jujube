f2=open('ld.prune.in','r')
f1=open('/home/lianqun/job_space/01_jujube_reseq/10_delete_TE/TE.excluded.snp.vcf','r')
p=open('ld.prune.filtered.vcf','w')

dict1={}

for eachline in f2:
	eachline=eachline.strip()
	dict1[eachline]=0

for eachline in f1:
	eachline=eachline.strip()
	if eachline[0]=='#':
		p.write(eachline+'\n')
	else:
		i=eachline.split()
		ID=i[0].split('_')[1]+'_'+i[1]
		if ID in dict1:
			p.write(eachline+'\n')
		else:
			continue
