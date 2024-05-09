#!/public/agis/huangsanwen_group/lintao/bin/python3
#Program name: genotype2ped_map.py
###Program information###
#	version: 1.0				author: lintao <lintao19870305@gmail.com>		date: 2015-03-11
"""
				module description
								version: 1.0 author: lintao <lintao19870305@gmail.com>		date: 2015-03-11
"""

#include the required module
import sys
import re
import os
import argparse


#command-line interface setting
parser = argparse.ArgumentParser(description = 'Tranforming genotype to hap and map format')
parser.add_argument('-i', type = argparse.FileType('r'), help = 'Input of genotype file')
parser.add_argument('-IND', type = argparse.FileType('r'), help = 'Input of individual ID file')
parser.add_argument('-o1', default = 'parser.out', type = argparse.FileType('w'), help = 'output of ped file')
parser.add_argument('-o2', default = 'parser.out', type = argparse.FileType('w'), help = 'output of map file')

args = parser.parse_args()


#global varialbe
debug = True


#class definition


#function definition
def Transform(input1, input2, output1, output2):			#I filter ',' in the column of ALT, zhou don't filter it.

	first_list = []
	IND_list = []
	
	for eachline in input2:		#individual ID file
		eachline = eachline.strip()
		if eachline[0] == '#':
			continue
		first_list = eachline.split()
		IND_list.append(first_list[0])
	#	output.write('{0} 1 0 0 1 2\n'.format(first_list[2]))
		
	second_list = []
	third_list = []
	forth_list = []
	dict_geno = {}
	dict_allele = {}
	dict_allele = {'A':'AA', 'G':'GG', 'T':'TT', 'C':'CC', '-':'00', 'K':'GT', 'S':'GC', 'Y':'TC', 'M':'AC', 'W':'AT', 'R':'GA'}

	for eachline in input1:		#genotype file
		eachline = eachline.strip()
		if eachline[0] == '#':
			continue
		second_list = eachline.split('\t')
		if 'N' in second_list[2] or 'H' in second_list[2] or 'B' in second_list[2] or 'D' in second_list[2] or 'V' in second_list[2]:
			continue
		third_list = re.split(' ', second_list[2])
		forth_list = re.split('a|r', second_list[0])
		for i in range(0, len(third_list)):
			if IND_list[i] not in dict_geno:
				dict_geno[IND_list[i]] = [third_list[i]]
			else:
				dict_geno[IND_list[i]].append(third_list[i])
#		print(forth_list)
		output2.write('{0} {1}_{2} 0 {3}\n'.format(forth_list[1], second_list[0], second_list[1], second_list[1]))
		
	for i in range(0, len(IND_list)):
		output1.write('{0} 1 0 0 1 2'.format(IND_list[i]))
		for j in range(0, len(dict_geno[IND_list[i]])):
			output1.write(' {0} {1}'.format(dict_allele[dict_geno[IND_list[i]][j]][0], dict_allele[dict_geno[IND_list[i]][j]][1]))
		output1.write('\n')
	
if __name__ == "__main__":

	Transform(args.i, args.IND, args.o1, args.o2)
	args.i.close()
	args.IND.close()
	args.o1.close()
	args.o2.close()
