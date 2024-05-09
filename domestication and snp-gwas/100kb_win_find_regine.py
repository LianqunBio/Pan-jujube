import os
import sys
import argparse

parser=argparse.ArgumentParser(description='find the regine sweep')
parser.add_argument('-i', type =argparse.FileType('r'),help='the file of top5_filter_sorted.poly')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True

lst=[]
a=1
flag=0
args.o.write('#Chromsome\tStart\tEnd\tLength(bp)\tpi_cul\tpi_wild\tpi_ratio\n')

for eachline in args.i:
	eachline = eachline.strip()
	i = eachline.split()
	if flag == 0:
		chr_ID = i[0]
		regine_start = int(i[1])
		chr_start =int(i[1])
		cul_pi =float(i[3])
		wild_pi =float(i[2])
		flag=1
	elif flag == 1:
		if i[0] == chr_ID:
			if (int(i[1])-(chr_start+100000)) <= 100000:
				cul_pi +=float(i[3])
				wild_pi +=float(i[2])
				a+=1
				chr_start = int(i[1])
			else:
				args.o.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n'.format(chr_ID,regine_start,chr_start+100000,chr_start+100000-regine_start,cul_pi/(a),wild_pi/(a),(wild_pi/(a))/(cul_pi/(a))))
				a=1
				chr_ID = i[0]
				regine_start = int(i[1])
				chr_start =int(i[1])
				cul_pi =float(i[3])
				wild_pi =float(i[2])
		else:
			args.o.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n'.format(chr_ID,regine_start,chr_start+100000,chr_start+100000-regine_start,cul_pi/(a),wild_pi/(a),(wild_pi/(a))/(cul_pi/(a))))
			a=1
			chr_ID = i[0]
			regine_start = int(i[1])
			chr_start =int(i[1])
			cul_pi =float(i[3])
			wild_pi =float(i[2])
args.o.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n'.format(chr_ID,regine_start,chr_start+100000,chr_start+100000-regine_start,cul_pi/(a),wild_pi/(a),(wild_pi/(a))/(cul_pi/(a))))
			
