### Domestication analysis
```
vcftools --gzvcf all.vcf.gz --window-pi 100000 --window-pi-step 10000 --out wild --keep wild.individual.list
vcftools --gzvcf all.vcf.gz --window-pi 100000 --window-pi-step 10000 --out cultivar --keep cultivated.individual.list
python3 merge.window.py -wild wild.windowed.pi -cul cultivar.windowed.pi -o all_ritio.poly
sort -k 6,6nr all_ritio.poly > sorted_all_ritio.poly
wc -l sorted_all_ritio.poly # get all the number of windows and calculate the value of top 5%
head -n 3654 sorted_all_ritio.poly | cut -f 1,2,4,5,6 > top5_sorted_all_ritio.poly
awk '{if ($3>0.001) print$0}' top5_sorted_all_ritio.poly > filter_top5_sorted_all_ritio.poly
sort -k 1,1 -k 2,2n filter_top5_sorted_all_ritio.poly > top5_Chr_pos_sorted_filterd_ritio.poly
python3 100kb_win_find_regine.py -i top5_Chr_pos_sorted_filterd_ritio.poly -o sweep_regine
python add_code.py
python3 find_gene_in_sweep_regine.py -i1 sweep-regine-info.xls -i2 Ref.gff3 -i3 Annotation.infor.txt -o gene_IN_sweep_regine.xls
# graph pai ratio and curve lines
for i in {01..12}; do grep chr$i ../all_ritio.poly > chr$i.raw.poly; done
for i in {01..12}; do grep chr$i ../sweep_regine > chr$i.sweep.regine; done
R < pai.curve.line.R --vanilla
R < pai_lines_graph.R --vanilla
```
### GWAS analysis

```
python3 extract.genotype.py -i all.genotype -all ALL.name.list -part part.name.list -o part.raw.genotype
python3 filter_genotype.py -i part.raw.genotype -o part.filtered.genotype
python3 genotype2ped_map.py -i part.filtered.genotype -IND part.name.list -o1 filterd_all.final.genotype.ped -o2 filterd_all.final.genotype.map
python change_format.py
mv tem filterd_all.final.genotype.map
plink --file filterd_all.final.genotype --recode12 --output-missing-genotype 0 --transpose --out filterd_all.final.genotype --noweb
java -jar -Xms256m -Xmx3300m gec.jar --effect-number --maf 0.05 --linkage-file filterd_all.final.genotype --genome --out filterd_all.final.genotype.effect # calculate threshold value
emmax-kin-intel64 -v -s -d 10 filterd_all.final.genotype
for i in `cat phenotype.list`; do emmax-intel64 -v -d 10 -t filterd_all.final.genotype -p $i -k filterd_all.final.genotype.aIBS.kinf -o $i.EMMAX; done

# graph Manhattan figure and qq-plot
python prepare_input_qqman.py -i output.EMMAX.ps -o input
/home/lianqun/miniconda3/bin/R < qqman.testversion2.R --vanilla
```
### FDR test for GWAS result
```
grep -v chr00 input.EMMAX.ps > inputfile.txt
~/miniconda3/bin/R < work.R --vanilla
grep -v x output.txt | paste inputfile.txt - > FDR.input.EMMAX.ps
```
### Extract candidate gene information
```
for i in `cat phenotype.list`; do python3 tet.gwas.candidate.genes.py -gwas FDR.$i.EMMAX.ps -the 5.5 -ann snp.annotation.all.result -gene genes.annotation.infor -o FDR.$i.out.xls ; done
```
