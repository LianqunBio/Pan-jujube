### Gene-based pangeome construction

```
python3 filter.len.py -i input.pep.fa -o output.pep.fa # filter the aa length shorted than 30
orthofinder -f pep.data -t 12 -a 50 -T iqtree -M msa -ot # all the genome used to construct the gene-based pan-genome were deposited in the dictory 'pep.data'
the files in dictory pep.data:
Dongzao.pep.fa
JunT2T.pep.fa
S21.pep.fa
SuanFLS.pep.fa
SuanT2T.pep.fa
Z203.pep.fa
Z94.pep.fa
Z95.pep.fa
most basic information was deposited in the file name "Statistics_Overall.tsv". Some other information used in paper can be extracted by the following scripts:
python3 get.proportion.py
python3 extract.freq.py
```

### ka/ks calculation
```
python3 select.longest.cds.py # select longest seq for each accessions in each orthogroup
python3 generate.homologs.file.py -group longest.tem1.Orthogroups.tsv # generate commands for each orthogroup, using this script, the following command will be printed
~/software/ParaAT2.0/ParaAT.pl -h homologs.file -n all.cds.line.fa -a all.pep.line.fa -p proc -m muscle -k -o Out.result -format axt
python3 split.value.py # statistic information with different genome number
python3 get.value.py # statistic information with different genome number
```
### FPKM calculation
```
python3 get.fpkm.diff.group.py -expression S21.merged.fpkm.xls -core ../core.group.list -dispensable ../dispensable.group.list -private ../private.group.list -orthogroups ../tem1.Orthogroups.tsv -tag S21 -outcore S21.core -outdispensable S21.dispensable -outprivate S21.private # statistic information with different genome number
```

### sequence pan-genome
```
~/software/minigraph/minigraph -xggs -t5 z95.fa z94.fa z203.fa s21.fa JunT2T.fa SuanFLS.fa SuanT2T.fa Dong.fa > all.out.gfa
```

