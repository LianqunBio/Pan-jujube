import os
import sys
import argparse

parser=argparse.ArgumentParser(description='filter the SNP data of the genotype')
parser.add_argument('-i', type =argparse.FileType('r'),help='the SNP data file')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True

zd={'A':'AA','T':'TT','C':'CC','G':'GG','W':'AT','S':'CG','K':'TG','M':'AC','Y':'CT','R':'AG','-':'--'}
lst_del=['V','D','B','H','N'] #to delete the snp point with three kinds of genotype
for eachline in args.i:
	str_loci=''
	eachline = eachline.strip()
	i = eachline.split('\t',2)
	loci_lst=i[2].split()
	for loci in loci_lst:
		if loci in lst_del:
			break
		else:
			if loci in zd:
				str_loci+=zd[loci]
			else:
				print('ERRO')
	num_NA = str_loci.count('-')
	if num_NA/len(str_loci) > 0.4:
		pass
	else:
		lst_set=list("".join(set(str_loci)))#convert str to list
		new_lst=[]
		for factor in lst_set:
			if factor == '-' or factor in new_lst:
				continue
			else:
				new_lst.append(factor)
		if len(new_lst) != 2:
			continue
		else:
			if str_loci.count(new_lst[0])/len(str_loci) < 0.05 or str_loci.count(new_lst[1])/len(str_loci) < 0.05:
				continue
			else:
				args.o.write(eachline+'\n')
