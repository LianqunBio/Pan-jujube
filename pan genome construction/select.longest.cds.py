f1=open('all.pep.line.fa','r') # cat all the pep file together with the format one line one seq
f2=open('tem1.Orthogroups.tsv','r') # sed 's/ //g' Orthogroups.tsv > tem1.Orthogroups.tsv
p=open('longest.tem1.Orthogroups.tsv','w') # select the longest cds seq for each sample

dict1={}
for eachline in f1:
	eachline=eachline.strip()
	if eachline:
		if eachline[0]=='>':
			ID=eachline[1:]
			dict1[ID]=0
		else:
			value=len(eachline)
			dict1[ID]=value

for eachline in f2:
	eachline=eachline.strip()
	i=eachline.split()
	if i[0]=='Orthogroup':
		p.write(eachline+'\n')
	else:
		groupID=i[0]
		if len(i)==2:
			if len(i[1].split(','))==2:
				p.write(eachline+'\n')
			else:
				newlst=i[1].split(',')
				vlst=[]
				for factor in newlst:
					vlst.append(dict1[factor])
				maxvalue=max(vlst)
				for factor in newlst:
					if dict1[factor]==maxvalue:
						outgene1=factor
				vlst.remove(maxvalue)
				Smaxvalue=max(vlst)
				for factor in newlst:
					if dict1[factor]==Smaxvalue:
						outgene2=factor
				p.write(i[0]+'\t'+outgene1+','+outgene2+'\n')

		else:
			strout=''
			for it in i:
				if it==groupID:
					continue
				else:
					if ',' not in it:
						strout+=it+'\t'
					else:
						lenvalue=0
						target=''
						for gene in it.split(','):
							if dict1[gene]>=lenvalue:
								lenvalue=dict1[gene]
								target=gene
							else:
								continue
						strout+=target+'\t'
			p.write(i[0]+'\t'+strout.strip()+'\n')
	


