import os
import sys
import argparse

parser=argparse.ArgumentParser(description='transform the file format from vcf to genotype')
parser.add_argument('-i', type =argparse.FileType('r'),help='the SNP data file')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True


dict1={'AG':'R','GA':'R','AC':'M','CA':'M','CT':'Y','TC':'Y','AT':'W','TA':'W','GC':'S','CG':'S','GT':'K','TG':'K'}

for eachline in args.i:
	eachline=eachline.strip()
	if eachline[0]=='#':
		continue
	else:
		i=eachline.split('\t',9)
		chrID=i[0]
		pos=i[1]
		code_lst=i[9].split()
		str_out=''
		ref=i[3]
		alt=i[4]
		for it in code_lst:
			infor=it.split(':')[0]
			if infor == '0/0' or infor=='0|0':
				str_out+=ref+' '
			elif infor=='1/1' or infor=='1|1':
				str_out+=alt+' '
			elif infor=='./.' or infor=='.|.':
				str_out+='-'+' '
			else:
				str_out+=dict1[ref+alt]+' '
		args.o.write(chrID+'\t'+pos+'\t'+str_out.strip()+'\n')
