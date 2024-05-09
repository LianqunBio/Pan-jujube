import os
import sys
import argparse

parser=argparse.ArgumentParser(description='merge the window in two groups')
parser.add_argument('-wild', type =argparse.FileType('r'),help='the wild group pai result')
parser.add_argument('-cul', type =argparse.FileType('r'),help='the cultivate group pai result')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True

dict1={}
for eachline in args.cul:
	eachline=eachline.strip()
	i=eachline.split()
	if i[0]=='CHROM':
		continue
	else:
		ID=i[0]+'\t'+i[1]
		dict1[ID]=i[4]


for eachline in args.wild:
	eachline = eachline.strip()
	i = eachline.split()
	if i[0]=='CHROM':
		continue
	else:
		ID=i[0]+'\t'+i[1]
		if ID not in dict1:
			continue
		else:
			wild_pi=float(i[4])
			ritio = wild_pi/float(dict1[ID])

			args.o.write('%s\t%s\t%s\t%s\t%s\t%f\n' % (i[0],i[1],i[2],i[4],dict1[ID],ritio))

