import os
import sys
import argparse

parser=argparse.ArgumentParser(description='extract part genotype from the whole genotype file')
parser.add_argument('-i', type =argparse.FileType('r'),help='the SNP data file')
parser.add_argument('-all', type =argparse.FileType('r'),help='the whole namelist file')
parser.add_argument('-part', type =argparse.FileType('r'),help='the part namelist file')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True

dict1={}
dict2={}
for eachline in args.part:
	eachline=eachline.strip()
	dict1[eachline]=0

index=0
for eachline in args.all:
	eachline=eachline.strip()
	i=eachline.split()
	if i[0] not in dict1:
		pass
	else:
		dict2[index]=0
	index+=1
	print(index)

for eachline in args.i:
	eachline=eachline.strip()
	i=eachline.split('\t')
	code_lst=i[2].split()
	str_out=''
	for index in range(0,len(code_lst)):
		if index in dict2:
			str_out+=code_lst[index]+' '
		else:
			continue
	args.o.write(i[0]+'\t'+i[1]+'\t'+str_out.strip()+'\n')
