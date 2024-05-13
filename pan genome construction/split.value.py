f=open('kaks.result.xls','r')
f1=open('./one.sample.list','r')
dict1={}
for eachline in f1:
	eachline=eachline.strip()
	dict1[eachline]=0
f2=open('./two.sample.list','r')
dict2={}
for eachline in f2:
	eachline=eachline.strip()
	dict2[eachline]=0
f3=open('./three.sample.list','r')
dict3={}
for eachline in f3:
	eachline=eachline.strip()
	dict3[eachline]=0
f4=open('./four.sample.list','r')
dict4={}
for eachline in f4:
	eachline=eachline.strip()
	dict4[eachline]=0
f5=open('./five.sample.list','r')
dict5={}
for eachline in f5:
	eachline=eachline.strip()
	dict5[eachline]=0
f6=open('./six.sample.list','r')
dict6={}
for eachline in f6:
	eachline=eachline.strip()
	dict6[eachline]=0
f7=open('./seven.sample.list','r')
dict7={}
for eachline in f7:
	eachline=eachline.strip()
	dict7[eachline]=0
f8=open('./eight.sample.list','r')
dict8={}
for eachline in f8:
	eachline=eachline.strip()
	dict8[eachline]=0

p1=open('one.out','w')
p2=open('two.out','w')
p3=open('three.out','w')
p4=open('four.out','w')
p5=open('five.out','w')
p6=open('six.out','w')
p7=open('seven.out','w')
p8=open('eight.out','w')

for eachline in f:
	eachline=eachline.strip()
	i=eachline.split()
	ID=i[0].split('.')[0]
	value=i[-1]
	if ID in dict1:
		p1.write(value+'\n')
	elif ID in dict2:
		p2.write(value+'\n')
	elif ID in dict3:
		p3.write(value+'\n')
	elif ID in dict4:
		p4.write(value+'\n')
	elif ID in dict5:
		p5.write(value+'\n')
	elif ID in dict6:
		p6.write(value+'\n')
	elif ID in dict7:
		p7.write(value+'\n')
	elif ID in dict8:
		p8.write(value+'\n')





