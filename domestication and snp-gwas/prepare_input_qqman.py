import os
import sys
import argparse

parser=argparse.ArgumentParser(description='prepare the input file for qqman to paint qqplot and manhattan plot graph')
parser.add_argument('-i', type =argparse.FileType('r'),help='the SNP data file')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True
# z95_chr12_28054370
args.o.write('SNP\tCHR\tBP\tP\n')
for eachline in args.i:
	eachline=eachline.strip()
	i=eachline.split()
	if (len(i)==4) and ('-nan' not in eachline) and ('z95_chr00' not in eachline):
		if i[0].split('_')[1]!='chr00':
			if i[0].split('_')[1][-2]=='0':
				snp_ID=i[0]
				chr_ID=i[0].split('_')[1][-1]
				pos_ID=i[0].split('_')[-1]
				p_value=i[3]
				if  float(p_value)>0: # change
					args.o.write('%s\t%s\t%s\t%s\n' % (snp_ID,chr_ID,pos_ID,p_value))
				else:
					print(p_value)
			else:
				snp_ID=i[0]
				chr_ID=i[0].split('_')[1][-2:]
				pos_ID=i[0].split('_')[-1]
				p_value=i[3]
				if  float(p_value) > 0:
					args.o.write('%s\t%s\t%s\t%s\n' % (snp_ID,chr_ID,pos_ID,p_value))
	else:
		continue
#		print(eachline)
