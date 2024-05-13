f=open('/home/lianqun/job_space/01_jujube_reseq/10_delete_TE/02_phy_tree/ld_prune/target.sample.phy','r')
p=open('out.fa','w')

for eachline in f:
	eachline=eachline.strip()
	i=eachline.split()
	if i[0]=='1062':
		continue
	else:
		p.write('>'+i[0]+'\n'+i[-1]+'\n')
