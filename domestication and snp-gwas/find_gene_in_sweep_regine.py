import os
import sys
import argparse

parser=argparse.ArgumentParser(description='find the gene of the regine sweep base on the annotation file')
parser.add_argument('-i1', type =argparse.FileType('r'),help='the sweep regine file')
parser.add_argument('-i2', type =argparse.FileType('r'),help='the annotation file')
parser.add_argument('-o', type =argparse.FileType('w'),help='the outputfile')

args=parser.parse_args()

debug=True


zd_pos={}
zd_infor={}
zd_length={}
for eachline in args.i2:
	eachline = eachline.strip()
	i=eachline.split('\t')
	if eachline[0]=='#':
		continue
	else:
		if i[2]!='gene' or i[0]=='ChrUn':
			continue
		else:
#	print(i[3])
			gene_ID=i[8].split(';')[0].split('=')[1]
			print(gene_ID)
			gene_infor=i[8].split('name=')[1][1:-1]
			zd_infor[gene_ID]=gene_infor
			zd_length[gene_ID]=i[3]+'\t'+i[4]+'\t'+str(int(i[4])+1-int(i[3]))
#			print(i[3])
#			for num in range(int(i[3]),int(i[4])+1):
			for index in range(int(i[3]),int(i[4])+1):
#			for index in range(0,20+1):
				ID=i[0]+'_'+str(index)
#				print(ID)
				zd_pos[ID]=gene_ID

for eachline in args.i1:
	eachline=eachline.strip()
	i=eachline.split()
	lst=[]
	sweep_ID=i[0].split('-')[0]
	chr_ID=i[0].split('-')[2]
	for num in range(int(i[1]),int(i[2])+1):
		ID=chr_ID+'_'+str(num)
		if ID in zd_pos:
			if zd_pos[ID] not in lst:
#				print(zd_pos[ID])
				lst.append(zd_pos[ID])
				if zd_pos[ID] in zd_infor:
					args.o.write('%s\t%s\t%s\t%s\t%s\n' % (chr_ID,zd_pos[ID],zd_length[zd_pos[ID]],sweep_ID,zd_infor[zd_pos[ID]]))
				else:
					args.o.write('%s\t%s\t%s\t%s\tNONE\n' % (chr_ID,zd_pos[ID],zd_length[zd_pos[ID]],sweep_ID))
			else:
				continue
		else:
			continue


	
