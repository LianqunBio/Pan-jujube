f1=open('1059.list.genotype','r')
f2=open('ld.prune.in','r')
p=open('ld.filterd.genotype','w')

dict1={}

for eachline in f2:
        eachline=eachline.strip()
        dict1[eachline]=0

for eachline in f1:
        eachline=eachline.strip()
        i=eachline.split()
        ID=i[0]+'_'+i[1]
        if ID in dict1:
                p.write(eachline+'\n')
        else:
                pass
