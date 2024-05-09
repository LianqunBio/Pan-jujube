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

