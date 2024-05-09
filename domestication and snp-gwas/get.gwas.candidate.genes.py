import os
import sys
import argparse
import math

parser=argparse.ArgumentParser(description='extract the gwas candidate genes')
parser.add_argument('-gwas', type =argparse.FileType('r'),help='the emmax gwas result file')
parser.add_argument('-the', type =float,help='the threshold')
parser.add_argument('-ann', type =argparse.FileType('r'),help='the snp annotation file')
parser.add_argument('-gene', type =argparse.FileType('r'),help='the gene annotation file')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True

dict_snp={}
dict_gene={}
args.o.write('Chr\tPos\tMutation-n\ttype\tGene\tMutation-aa\tpvalue\tChr\tStart\tEnd\tn_seq\taa_seq\tAth-gene\tAth-idendity\tAth-evalue\tRice-gene\tRice-idendity\tRice-evalue\tDong-gene\tDong-idendity\tDong-evalue\tZ95-BS-1\tZ95-EF-1\tZ95-flower-1\tZ95-leaf-1\tZ95-MF-1\tZ95-phloem-1\tZ95-stem-1\tZ95-YF-1\tAnnotation\n')

for eachline in args.ann:
	eachline=eachline.strip()
	i=eachline.split('\t',2)
	ID=i[0]+'_'+i[1]
	dict_snp[ID]=eachline

for eachline in args.gene:
	eachline=eachline.strip()
	i=eachline.split('\t',1)
	ID=i[0].split('.')[0]
	dict_gene[ID]=i[1]

threshold=args.the
for eachline in args.gwas:
	eachline=eachline.strip()
	i=eachline.split()
	SNP=i[0]
	value=-math.log(float(i[-1]),10)
#	print(value)
	if SNP not in dict_snp:
		print(SNP)
	else:
		if value>=args.the:
			list1=dict_snp[SNP].split()
			if '-' in list1[-2]:
				geneID1=list1[-2].split('-')[0]
				geneID2=list1[-2].split('-')[1]
				args.o.write(dict_snp[SNP]+'\t'+str(value)+'\t'+dict_gene[geneID1]+'\n')
				args.o.write(dict_snp[SNP]+'\t'+str(value)+'\t'+dict_gene[geneID2]+'\n')
			else:
				geneID=list1[-2]
				args.o.write(dict_snp[SNP]+'\t'+str(value)+'\t'+dict_gene[geneID]+'\n')
