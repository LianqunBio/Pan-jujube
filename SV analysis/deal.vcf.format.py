import os
import sys
import argparse

parser=argparse.ArgumentParser(description='transform the vcf format for merging')
parser.add_argument('-syri', type =argparse.FileType('r'),help='the vcf output file')
parser.add_argument('-Ref', type =argparse.FileType('r'),help='the ref genome file')
parser.add_argument('-Alt', type =argparse.FileType('r'),help='the alt genome file')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of snp file')

args=parser.parse_args()

debug=True

dictref={}
dictalt={}

flag=0
for eachline in args.Ref:
	eachline=eachline.strip()
	if flag==0:
		if eachline[0]=='>':
			ID=eachline[1:]
			dictref[ID]=''
			strout=''
			flag=1
	else:
		if eachline[0]!='>':
			strout+=eachline
		else:
			dictref[ID]=strout
			ID=eachline[1:]
			dictref[ID]=''
			strout=''
dictref[ID]=strout

flag=0
for eachline in args.Alt:
	eachline=eachline.strip()
	if flag==0:
		if eachline[0]=='>':
			ID=eachline[1:]
			dictalt[ID]=''
			strout=''
			flag=1
	else:
		if eachline[0]!='>':
			strout+=eachline
		else:
			dictalt[ID]=strout
			ID=eachline[1:]
			dictref[ID]=''
			strout=''
dictalt[ID]=strout

target=['INV','DUP','INS','DEL','CPG','CPL']
for eachline in args.syri:
	eachline=eachline.strip()
	i=eachline.split()
	if eachline[0]=='#':
		args.o.write(eachline+'\n')
	else:
		if ('AL' in i[2]) or ('SNP' in i[2]):
			continue
		else:
			if '<' not in i[4]:
				if abs(len(i[3])-len(i[4]))>=50:
					args.o.write(eachline+'\n')
				else:
					continue
			else:
				svtype=i[4][1:-1]
				if svtype not in target:
					continue
				else:
					refchr=i[0]
					refstart=min(int(i[1])-1,int(i[7].split(';')[0].split('=')[1]))
					refend=max(int(i[1])-1,int(i[7].split(';')[0].split('=')[1]))
					altchr=i[7].split(';')[1].split('=')[1]
					altstart=min(int(i[7].split(';')[2].split('=')[1])-1,int(i[7].split(';')[3].split('=')[1]))
					altend=max(int(i[7].split(';')[2].split('=')[1])-1,int(i[7].split(';')[3].split('=')[1]))
					refseq=dictref[refchr][refstart:refend]
					altseq=dictalt[altchr][altstart:altend]
					args.o.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],refseq,altseq,i[5],i[6],i[7]))














