### Step1 Construct neighbour-joining phylogenetic tree utilizing all the snp loci (TE-excluded)

```
~/software/VCF2Dis-1.50/bin/VCF2Dis -i input.vcf -o p_dis.mat -s sample.list # calculate the distance matrix using software VCF2Dis
phylip neighbor # For getting NJ-tree, we employed phylip-neigbor algorithm, the parameter are followed
p_dis.mat # input file name
I # for sequential format file
O # set outgroup sample
1509 # the number of outgroup sample
Y # accept all the parameter setting
```
The output newick file by phylip can be uploaded into software MEGA6.0 for further adjusting and coloring.

### Step2 Structure analysis utilizing all the snp loci (TE-excluded) after LD-pruned

```
python3 genotype2ped_map.py -i input.snp.genotype -IND sample.list  -o1 example.ped -o2 example.map
plink --file example --make-bed --out example
plink --file example --indep-pairwise 50 10 0.2 --out ld # LD-pruning using software PLINK
python merge.py # extract the overlapping loci information
python3 genotype2ped_map.py -i ld.filterd.genotype -IND sample.list -o1 ld.miss.filterd.example.ped -o2 ld.miss.filterd.example.map
plink --file ld.miss.filterd.example --make-bed --out ld.miss.filterd.example
admixture -j3 --cv ld.miss.filterd.example.bed 2 | tee log2.out
admixture -j3 --cv ld.miss.filterd.example.bed 3 | tee log3.out
admixture -j3 --cv ld.miss.filterd.example.bed 4 | tee log4.out
admixture -j3 --cv ld.miss.filterd.example.bed 5 | tee log5.out
admixture -j3 --cv ld.miss.filterd.example.bed 6 | tee log6.out
admixture -j3 --cv ld.miss.filterd.example.bed 7 | tee log7.out
admixture -j3 --cv ld.miss.filterd.example.bed 8 | tee log8.out
admixture -j3 --cv ld.miss.filterd.example.bed 9 | tee log9.out
admixture -j3 --cv ld.miss.filterd.example.bed 10 | tee log10.out
admixture -j3 --cv ld.miss.filterd.example.bed 11 | tee log11.out
admixture -j3 --cv ld.miss.filterd.example.bed 12 | tee log12.out
admixture -j3 --cv ld.miss.filterd.example.bed 13 | tee log13.out
admixture -j3 --cv ld.miss.filterd.example.bed 14 | tee log14.out
admixture -j3 --cv ld.miss.filterd.example.bed 15 | tee log15.out
admixture -j3 --cv ld.miss.filterd.example.bed 16 | tee log16.out
admixture -j3 --cv ld.miss.filterd.example.bed 17 | tee log17.out
admixture -j3 --cv ld.miss.filterd.example.bed 18 | tee log18.out
admixture -j3 --cv ld.miss.filterd.example.bed 19 | tee log19.out
admixture -j3 --cv ld.miss.filterd.example.bed 20 | tee log20.out
```
Output file can be visulized by Excel.

### Step3 PCA analysis (TE-excluded)

```
python3 for_genotype.py -i filtered.genotype -o1 genotype -o2 SNP_info
~/software/EIG-7.2.1/src/eigensrc/smartpca -p zao_par # zao_par: the configuration file
perl ~/software/EIG-6.0.1/bin/ploteig -i zao.evec -c 1:2 -p Wild:Cultivated:Cultivated_Subgroup_I:Cultivated_Subgroup_II:Cultivated_Subgroup_III:Cultivated_Subgroup_IV -x -o zao.xtxt # -p group information (identified according to the result by phylogenetic tree and admixture) # graphing with PC1 and PC2

```
zao_par configuaratioin file :
```
genotypename: genotype
snpname: SNP_info
indivname: sample.information
evecoutname: zao.evec
evaloutname: zao.eval
altnormstyle: NO
numoutevec: 10
numoutlieriter: 0
numoutlierevec: 10
outliersigmathresh: 6
qtmode: 0
```


### Step4 LD-decay analysis using all the snp loci (TE-excluded)
```
PopLDdecay -InVCF  all.snp.vcf.gz  -OutStat Wild.stat.gz -SubPop Wild.list
PopLDdecay -InVCF  all.snp.vcf.gz  -OutStat C-Sub1.stat.gz -SubPop C-Sub1.list
PopLDdecay -InVCF  all.snp.vcf.gz  -OutStat C-Sub2.stat.gz -SubPop C-Sub2.list
PopLDdecay -InVCF  all.snp.vcf.gz  -OutStat C-Sub3.stat.gz -SubPop C-Sub3.list
PopLDdecay -InVCF  all.snp.vcf.gz  -OutStat C-Sub4.stat.gz -SubPop C-Sub4.list
PopLDdecay -InVCF  all.snp.vcf.gz  -OutStat C-Sub4.stat.gz -SubPop C-Sub4.list

~/software/PopLDdecay-3.41/bin/Plot_MultiPop.pl -inList  file.list  -output Fig # graph LD-decay figure.  file.list as follows:
~/Wild.stat.gz	Wild
~/C-Sub1.stat.gz C-Sub1
~/C-Sub2.stat.gz C-Sub2
~/C-Sub3.stat.gz C-Sub3
~/C-Sub4.stat.gz C-Sub4
~/C-Sub5.stat.gz C-Sub1
```

