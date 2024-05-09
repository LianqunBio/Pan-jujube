import os
import sys
import argparse

parser=argparse.ArgumentParser(description='creat three input files for the software EIG')
parser.add_argument('-i', type =argparse.FileType('r'),help='the SNP data from GWAS')
parser.add_argument('-o1', type =argparse.FileType('w'),help='the genetype file')
parser.add_argument('-o2', type =argparse.FileType('w'),help='the file includes SNP info')

args=parser.parse_args()

debug=True

lst_n=['A','T','C','G']
for eachline in args.i:
	eachline=eachline.strip()
	i = eachline.split('\t')
	name=i[0]+'_'+i[1]
	if i[0][3]=='0':
		Chr_ID=i[0][4:]
	else:
		Chr_ID=i[0][3:]
	pos=i[1]
#	args.o2.write('%s\t%s\t0.0\t%s\n' % (name,Chr_ID,pos))
	loci=i[2].split()
	str_loci=''
	str_out=''
	for e in loci:
		str_out+=e
		if e=='-' or e in str_loci:
#			print('B')
			continue
		else:
#			print('A')
			str_loci+=e
	if len(str_loci)==2:
		str_out=str_out.replace(str_loci[0],'0')
		str_out=str_out.replace(str_loci[1],'2')
		str_out=str_out.replace('-','9')
		args.o1.write(str_out+'\n')
		args.o2.write('%s\t%s\t0.0\t%s\n' % (name,Chr_ID,pos))
	elif len(str_loci)==3:
#		print(str_loci)
		if str_loci[0] not in lst_n:
			str_out=str_out.replace(str_loci[0],'1')
			str_out=str_out.replace(str_loci[1],'0')
			str_out=str_out.replace(str_loci[2],'2')
			str_out=str_out.replace('-','9')
			args.o1.write(str_out+'\n')
			args.o2.write('%s\t%s\t0.0\t%s\n' % (name,Chr_ID,pos))
		elif str_loci[1] not in lst_n:
			str_out=str_out.replace(str_loci[1],'1')
			str_out=str_out.replace(str_loci[0],'0')
			str_out=str_out.replace(str_loci[2],'2')
			str_out=str_out.replace('-','9')
			args.o1.write(str_out+'\n')
			args.o2.write('%s\t%s\t0.0\t%s\n' % (name,Chr_ID,pos))
		elif str_loci[2] not in lst_n:
			str_out=str_out.replace(str_loci[0],'0')
			str_out=str_out.replace(str_loci[1],'2')
			str_out=str_out.replace(str_loci[2],'1')
			str_out=str_out.replace('-','9')
			args.o1.write(str_out+'\n')
			args.o2.write('%s\t%s\t0.0\t%s\n' % (name,Chr_ID,pos))
		else:
			print(i[1])
	else:
		print(i[1])
		continue

