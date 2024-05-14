### Genome survey

```
jellyfish count -m 19 -s 500000000 -t 1 -o kmer_counts input.fq
jellyfish histo -h 100000 -t 1 kmer_counts > k19.reads.histo
# upload the result file to online website: http://qb.cshl.edu/genomescope/genomescope2.0/analysis for visualization
```
### Genome assembly

```
~/software/hifiasm-master/hifiasm -t 10 -o out.asm2 --primary --h1 FDHC210000858-1a_L1_1_clean.rd.fq.gz --h2 FDHC210000858-1a_L1_2_clean.rd.fq.gz  input.HiFi.fq > asm.log
```

### BUSCO evaluation for genome 

```
~/miniconda3/envs/py27/bin/busco -i input.contig.fa  -l embryophyta_odb10 -o out.busco -m geno
```

### LAI assessment for genome

```
~/software/LTR_FINDER_parallel-1.1/bin/LTR_FINDER.x86_64-1.0.7/ltr_finder  -C -D 15000 -d 1000 -L 7000 -l 100 -p 20 -M 0.85 Ref.fa > out.scn
~/software/LTR_retriever-master/LTR_retriever -threads 10 -genome Ref.fa -infinder out.scn
```

### Genome anchoring

```
~/software/juicer-master/scripts/juicer.sh -g SampleID -d ~/03_anchor/01-Z95-v2 -D ~/software/juicer-master -z SampleID.contig.version2.fa -p chr.len.file -t 5
~/software/3d-dna-master/run-asm-pipeline.sh -r 0 ./reference/SampleID.contig.version2.fa ./aligned/merged_nodups.txt
~/software/3d-dna-master/run-asm-pipeline-post-review.sh -r SampleID-check2.filterd.0.review.assembly ./reference/SampleID.filterd.fa ./aligned/merged_nodups.txt  > rerun.log
```
