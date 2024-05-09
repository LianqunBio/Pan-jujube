### Step1 Constructing neighbour-joining phylogenetic tree utilizing all the snp loci

```
~/software/VCF2Dis-1.50/bin/VCF2Dis -i input.vcf -o p_dis.mat -s sample.list # calculating the distance matrix using software VCF2Dis
phylip neighbor # For getting NJ-tree, we employed phylip-neigbor algorithm, the parameter are followed
p_dis.mat # input file name
I # for sequential format file
O # set outgroup sample
1509 # the number of outgroup sample
Y # accept all the parameter setting
```
The output newick file by phylip can be uploaded into software MEGA6.0 for further adjusting and coloring.

### Step2 Structure analysis utilizing all the snp loci after LD-pruned

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
