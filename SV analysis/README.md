### genome alignment and SV detection
```
nucmer --maxmatch -t 5 -c 90 -l 50 Ref.fa Query.Chr$i.fa # To accelerate the process, the query genome can be splited into chromosome.
delta-filter -i 90 -l 100 -r -q out.delta > delta.filter
cat  *delta.filter > all.delta.filter
show-coords -THrd  all.delta.filter > all.filtered.coords # all.delta.filter means the merged result from all the chromosome result.
python3 ~/softwares/syri1.5/bin/syri -c all.filtered.coords -d all.delta.filter -r Ref.fa -q Query.fa
```
### Domestication-related SVs

```
python3 overlap.py # Here, overlap the sweep region information and detected SVs between Z95 (Cultivate) and S21 (Wild)
python3 annotation.SV.py -vcf domestication.all.SV.vcf.xls -gff3 Ref.gff3 -o domestication.sv.annotation.out
```
### SV merging and pop-sv detection

```
python3 deal.vcf.format.py -syri  SampleID.syri.vcf -Ref  Ref.fa -Alt Qeury.fa -o SampleID.out # only extract 'DUP','INS','DEL','CPG','CPL'
SURVIVOR merge inputfile 100 1 1 0 0 50 merged.vcf # merge all the vcf
python3 ~/miniconda3/pkgs/paragraph-2.3-h8908b6f_0/bin/multigrmpy.py -i merged.vcf -m mfile -r Ref.fa -o output --threads 5 # mfile contains the file path, depth and reads length information of all the bam file used to genotyping the reference-based SV
```
### SV-gwas
```
python3 transfer.sv.py # transform the sv genotype file to snp genotype format for GWAS analysis
python extract.genotype.py -i sv.genotype -all all.name.list -part part.name.list -o part.raw.genotype
python3 filter_genotype.py -i part.raw.genotype -o part.filtered.genotype
python3 genotype2ped_map.py -i part.filtered.genotype -IND part.name.list -o1 filterd_all.final.genotype.ped -o2 filterd_all.final.genotype.map
python change_format.py
mv tem filterd_all.final.genotype.map
plink --file filterd_all.final.genotype --recode12 --output-missing-genotype 0 --transpose --out filterd_all.final.genotype --noweb
emmax-kin-intel64 -v -s -d 10 filterd_all.final.genotype
for i in `cat pheno.list` ; do echo emmax-intel64 -v -d 10 -t filterd_all.final.genotype -p $i.out -k filterd_all.final.genotype.aIBS.kinf -o $i.EMMAX; done
```



