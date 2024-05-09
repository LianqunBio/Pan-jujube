import os
import sys
import argparse

parser=argparse.ArgumentParser(description='calculate the ritio of pai_value')
parser.add_argument('-i', type =argparse.FileType('r'),help='the file of top5_filter_sorted.poly')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True


for eachline in args.i:
	eachline = eachline.strip()
	i = eachline.split()
	cul_pi = float(i[2])
	wild_pi = float(i[5])
	if cul_pi ==0 or wild_pi ==0:
		continue
	else:
		ritio = wild_pi/cul_pi
		args.o.write('%s\t%f\n' % (eachline,ritio))

