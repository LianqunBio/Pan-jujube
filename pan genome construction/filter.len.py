import os
import sys
import argparse

parser=argparse.ArgumentParser(description='filter the gene length with threshold of 30aa')
parser.add_argument('-i', type =argparse.FileType('r'),help='the input pep file')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True

flag=0
dict1={}
for eachline in args.i:
	eachline=eachline.strip()
	if eachline:
		if eachline[0]=='>':
			ID=eachline[1:]
			dict1[ID]=''
		else:
			dict1[ID]+=eachline

for it in dict1:
	if len(dict1[it])>30:
		args.o.write('>'+it+'\n'+dict1[it]+'\n')
	else:
		continue
