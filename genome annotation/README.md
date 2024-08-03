## Genome annotation mainly refered the pipeline: https://github.com/baozg/assembly-annotation-pipeline


## EDTA repeat annotation
export PATH=~/miniconda3/envs/EDTA/bin:$PATH
perl ~/software/EDTA/EDTA.pl --genome input.fa  --overwrite 1 --sensitive 1 --anno 1  --threads 30 --repeatmasker ~/software/RepeatMasker_4.10/v2_RepeatMasker > EDTA.logfile

## RNA-Seq assembly

### Hisat2 index-building
```
hisat2-build -p 20 input.fa input
```

### Hisat2 mapping
```
fastp -a auto --adapter_sequence_r2 auto --detect_adapter_for_pe -w 4 -i rawdata.R1.fastq.gz -I rawdata.R2.fastq.gz --n_base_limit 5 --cut_window_size 4 --cut_mean_quality 20 --length_required 75 --qualified_quality_phred 15 -o RNAseq.R1.gz -O RNAseq.R2.gz --json out..QC.fastp.json --html out.QC.fastp.html # RNA-seq data filtering
hisat2 -p 40 -x ~/path/to/input --rna-strandness RF -1 RNAseq.R1.gz -2 RNAseq.R2.gz -S OUT.sam 
samtools view -@ 2 -b -o OUT.bam OUT.sam
samtools sort -o OUT.sorted.bam -T OUT_temp --threads 2 OUT.bam
samtools merge all_sorted.bam tissue1.sorted.bam tissue2.sorted.bam tissue3.sorted.bam …… tissueN.sorted.bam
```

### Stringtie assembly
```
stringtie -p 6 --rf -l wildcards.sample -o output.gtf input.bam # run stringtie for each tissue
taco_run -o output_directory gff.file.txt # merge all the gtf using TACO
gffread all_stringtie.gtf -o all_stringtie.gff3
```
## Braker2 prediction
```
braker.pl --cores=48 --overwrite --species=Jujube --genome=input.softmask.fa --bam=all_sorted.bam --softmasking --gff3 
```
## 2. Run maker
```
ln -s ~/input.genome.fa.mod.EDTA.TElib.fa ./
ln -s ~/stringtie/all_stringtie.gff3 ./
ln -s ~/input.fa ./
ln -s ~/published.jujube.pep.fa ./
ln -s ~/published.jujube.pep.fa ./
ln -s ~/published.jujube.pep.fa ./
```

### Round 1

#### Generate config file
```
maker -CTL
```
#### round1_maker_opts.ctl
```
#-----Genome (these are always required)
genome=input.fa #genome sequence (fasta file or fasta embeded in GFF3 file)
organism_type=eukaryotic #eukaryotic or prokaryotic. Default is eukaryotic

#-----Re-annotation Using MAKER Derived GFF3
maker_gff= #MAKER derived GFF3 file
est_pass=1 #use ESTs in maker_gff: 1 = yes, 0 = no
altest_pass=1 #use alternate organism ESTs in maker_gff: 1 = yes, 0 = no
protein_pass=1 #use protein alignments in maker_gff: 1 = yes, 0 = no
rm_pass=1 #use repeats in maker_gff: 1 = yes, 0 = no
model_pass=1 #use gene models in maker_gff: 1 = yes, 0 = no
pred_pass=1 #use ab-initio predictions in maker_gff: 1 = yes, 0 = no
other_pass=1 #passthrough anyything else in maker_gff: 1 = yes, 0 = no

#-----EST Evidence (for best results provide a file for at least one)
est=Stringtie.fasta #set of ESTs or assembled mRNA-seq in fasta format
altest= #EST/cDNA sequence file in fasta format from an alternate organism
est_gff=all_stringtie.gff #aligned ESTs or mRNA-seq from an external GFF3 file
altest_gff= #aligned ESTs from a closly relate species in GFF3 format

#-----Protein Homology Evidence (for best results provide a file for at least one)
protein=published.jujube.pep.fa,published.jujube.pep.fa,published.jujube.pep.fa
protein_gff=  #aligned protein homology evidence from an external GFF3 file

#-----Repeat Masking (leave values blank to skip repeat masking)
model_org= #select a model organism for RepBase masking in RepeatMasker
rmlib=jujube.genome.fa.mod.EDTA.TElib.fa #provide an organism specific repeat library in fasta format for RepeatMasker
repeat_protein=~/software/maker/2.31.11/data/te_proteins.fasta #provide a fasta file of transposable element proteins for RepeatRunner
rm_gff=
prok_rm=0 #forces MAKER to repeatmask prokaryotes (no reason to change this), 1 = yes, 0 = no
softmask=1 #use soft-masking rather than hard-masking in BLAST (i.e. seg and dust filtering)

#-----Gene Prediction
snaphmm= #SNAP HMM file
gmhmm= #GeneMark HMM file
augustus_species= #Augustus gene prediction species model
fgenesh_par_file= #FGENESH parameter file
pred_gff= #ab-initio predictions from an external GFF3 file
model_gff= #annotated gene models from an external GFF3 file (annotation pass-through)
est2genome=1 #infer gene predictions directly from ESTs, 1 = yes, 0 = no
protein2genome=1 #infer predictions from protein homology, 1 = yes, 0 = no
trna=0 #find tRNAs with tRNAscan, 1 = yes, 0 = no
snoscan_rrna= #rRNA file to have Snoscan find snoRNAs
unmask=0 #also run ab-initio prediction programs on unmasked sequence, 1 = yes, 0 = no

#-----Other Annotation Feature Types (features MAKER doesn't recognize)
other_gff= #extra features to pass-through to final MAKER generated GFF3 file

#-----External Application Behavior Options
alt_peptide=C #amino acid used to replace non-standard amino acids in BLAST databases
cpus=1 #max number of cpus to use in BLAST and RepeatMasker (not for MPI, leave 1 when using MPI)

#-----MAKER Behavior Options
max_dna_len=100000 #length for dividing up contigs into chunks (increases/decreases memory usage)
min_contig=10000 #skip genome contigs below this length (under 10kb are often useless)

pred_flank=200 #flank for extending evidence clusters sent to gene predictors
pred_stats=0 #report AED and QI statistics for all predictions as well as models
AED_threshold=1 #Maximum Annotation Edit Distance allowed (bound by 0 and 1)
min_protein=0 #require at least this many amino acids in predicted proteins
alt_splice=0 #Take extra steps to try and find alternative splicing, 1 = yes, 0 = no
always_complete=0 #extra steps to force start and stop codons, 1 = yes, 0 = no
map_forward=0 #map names and attributes forward from old GFF3 genes, 1 = yes, 0 = no
keep_preds=0 #Concordance threshold to add unsupported gene prediction (bound by 0 and 1)

split_hit=10000 #length for the splitting of hits (expected max intron size for evidence alignments)
single_exon=0 #consider single exon EST evidence when generating annotations, 1 = yes, 0 = no
single_length=250 #min length required for single exon ESTs if 'single_exon is enabled'
correct_est_fusion=0 #limits use of ESTs in annotation to avoid fusion genes

tries=2 #number of times to try a contig if there is a failure for some reason
clean_try=0 #remove all data from previous run before retrying, 1 = yes, 0 = no
clean_up=0 #removes theVoid directory with individual analysis files, 1 = yes, 0 = no
TMP= #specify a directory other than the system default temporary directory for temporary files


mpiexec -n 40 maker -base jujube_round1 round1_maker_opts.ctl maker_bopts.ctl maker_exe.ctl


gff3_merge -s -d jujube_round1_master_datastore_index.log > jujube_rnd1.all.maker.gff
fasta_merge -d jujube_round1_master_datastore_index.log
gff3_merge -n -s -d jujube_round1_master_datastore_index.log > jujube_rnd1.all.maker.noseq.gff
cat jujube_rnd1.all.maker.gff | awk '{ if ($3 == "gene") print $0 }' | awk '{ sum += ($5 - $4) } END { print NR, sum / NR }'
perl ~/AED_cdf_generator.pl -b 0.5 jujube_rnd1.all.maker.gff
```
#### snap round1
```
maker2zff -c 0.8 -e 0.8 -o 0.8 -x 0.2 -l 50 -d ~/jujube_round1.maker.output/jujube_round1_master_datastore_index.log
mv genome.dna jujube_round1.zff.length50_aed0.25.dna
mv genome.ann jujube_round1.zff.length50_aed0.25.ann
# gather some stats and validate
fathom jujube_round1.zff.length50_aed0.25.ann jujube_round1.zff.length50_aed0.25.dna -gene-stats > gene-stats.log 2>&1
fathom jujube_round1.zff.length50_aed0.25.ann jujube_round1.zff.length50_aed0.25.dna -validate > validate.log 2>&1
# collect the training sequences and annotations, plus 1000 surrounding bp for training
fathom jujube_round1.zff.length50_aed0.25.ann jujube_round1.zff.length50_aed0.25.dna -categorize 1000 > categorize.log 2>&1
fathom uni.ann uni.dna -export 1000 -plus > uni-plus.log 2>&1
# create the training parameters
forge ../export.ann ../export.dna > ../forge.log 2>&1
# assembly the HMM
hmm-assembler.pl jujube_round1.zff.length50_aed0.25 params > jujube_round1.zff.length50_aed0.25.hmm
```

#### Round 2

round2_maker_opts.ctl:

```
#-----Genome (these are always required)
genome=~/jujube_anno/maker/input.fa #genome sequence (fasta file or fasta embeded in GFF3 file)
organism_type=eukaryotic #eukaryotic or prokaryotic. Default is eukaryotic

#-----Re-annotation Using MAKER Derived GFF3
maker_gff=~/jujube_rnd1.all.maker.gff #MAKER derived GFF3 file
est_pass=1 #use ESTs in maker_gff: 1 = yes, 0 = no
altest_pass=1 #use alternate organism ESTs in maker_gff: 1 = yes, 0 = no
protein_pass=1 #use protein alignments in maker_gff: 1 = yes, 0 = no
rm_pass=1 #use repeats in maker_gff: 1 = yes, 0 = no
model_pass=1 #use gene models in maker_gff: 1 = yes, 0 = no
pred_pass=1 #use ab-initio predictions in maker_gff: 1 = yes, 0 = no
other_pass=1 #passthrough anyything else in maker_gff: 1 = yes, 0 = no

#-----EST Evidence (for best results provide a file for at least one)
est= #set of ESTs or assembled mRNA-seq in fasta format
altest= #EST/cDNA sequence file in fasta format from an alternate organism
est_gff= #aligned ESTs or mRNA-seq from an external GFF3 file
altest_gff= #aligned ESTs from a closly relate species in GFF3 format

#-----Protein Homology Evidence (for best results provide a file for at least one)
protein= #protein sequence file in fasta format (i.e. from mutiple oransisms)
protein_gff=  #aligned protein homology evidence from an external GFF3 file

#-----Repeat Masking (leave values blank to skip repeat masking)
model_org= #select a model organism for RepBase masking in RepeatMasker
rmlib= #provide an organism specific repeat library in fasta format for RepeatMasker
repeat_protein= #provide a fasta file of transposable element proteins for RepeatRunner
rm_gff=
prok_rm=0 #forces MAKER to repeatmask prokaryotes (no reason to change this), 1 = yes, 0 = no
softmask=1 #use soft-masking rather than hard-masking in BLAST (i.e. seg and dust filtering)

#-----Gene Prediction
snaphmm=~/maker/snap/round1/jujube_round1.zff.length50_aed0.25.hmm #SNAP HMM file
gmhmm= #GeneMark HMM file
augustus_species=jujube_asiatica #Augustus gene prediction species model
fgenesh_par_file= #FGENESH parameter file
pred_gff= #ab-initio predictions from an external GFF3 file
model_gff= #annotated gene models from an external GFF3 file (annotation pass-through)
est2genome=0 #infer gene predictions directly from ESTs, 1 = yes, 0 = no
protein2genome=0 #infer predictions from protein homology, 1 = yes, 0 = no
trna=0 #find tRNAs with tRNAscan, 1 = yes, 0 = no
snoscan_rrna= #rRNA file to have Snoscan find snoRNAs
unmask=0 #also run ab-initio prediction programs on unmasked sequence, 1 = yes, 0 = no

#-----Other Annotation Feature Types (features MAKER doesn't recognize)
other_gff= #extra features to pass-through to final MAKER generated GFF3 file

#-----External Application Behavior Options
alt_peptide=C #amino acid used to replace non-standard amino acids in BLAST databases
cpus=1 #max number of cpus to use in BLAST and RepeatMasker (not for MPI, leave 1 when using MPI)

#-----MAKER Behavior Options
max_dna_len=100000 #length for dividing up contigs into chunks (increases/decreases memory usage)
min_contig=10000 #skip genome contigs below this length (under 10kb are often useless)

pred_flank=200 #flank for extending evidence clusters sent to gene predictors
pred_stats=0 #report AED and QI statistics for all predictions as well as models
AED_threshold=1 #Maximum Annotation Edit Distance allowed (bound by 0 and 1)
min_protein=0 #require at least this many amino acids in predicted proteins
alt_splice=0 #Take extra steps to try and find alternative splicing, 1 = yes, 0 = no
always_complete=0 #extra steps to force start and stop codons, 1 = yes, 0 = no
map_forward=0 #map names and attributes forward from old GFF3 genes, 1 = yes, 0 = no
keep_preds=0 #Concordance threshold to add unsupported gene prediction (bound by 0 and 1)

split_hit=10000 #length for the splitting of hits (expected max intron size for evidence alignments)
single_exon=0 #consider single exon EST evidence when generating annotations, 1 = yes, 0 = no
single_length=250 #min length required for single exon ESTs if 'single_exon is enabled'
correct_est_fusion=0 #limits use of ESTs in annotation to avoid fusion genes

tries=2 #number of times to try a contig if there is a failure for some reason
clean_try=0 #remove all data from previous run before retrying, 1 = yes, 0 = no
clean_up=0 #removes theVoid directory with individual analysis files, 1 = yes, 0 = no
TMP= #specify a directory other than the system default temporary directory for temporary files

mpiexec -n 40 maker -base jujube_round2 round2_maker_opts.ctl maker_bopts.ctl maker_exe.ctl

cd jujube_round2.maker.output
gff3_merge -s -d jujube_round2_master_datastore_index.log > jujube_rnd2.all.maker.gff
fasta_merge -d jujube_round2_master_datastore_index.log
gff3_merge -n -s -d jujube_round2_master_datastore_index.log > jujube_rnd2.all.maker.noseq.gff
cat jujube_rnd2.all.maker.gff | awk '{ if ($3 == "gene") print $0 }' | awk '{ sum += ($5 - $4) } END { print NR, sum / NR }'
perl ../AED_cdf_generator.pl -b 0.5 jujube_rnd2.all.maker.gff
```


