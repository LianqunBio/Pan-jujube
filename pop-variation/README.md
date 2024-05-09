### Step1, creating index file for reference genome

```
java -jar ~/software/picard-tools-1.118/CreateSequenceDictionary.jar R=Ref.fa O=Ref.dict
samtools faidx Ref.fa
bwa index Ref.fa
```

### Step2, mapping whole-genome-sequencing data to reference genome and get gvcf file for each sample

```
bwa mem -M -R  "@RG\tID:SampleID\tLB:SampleID\tPL:ILLUMINA\tSM:SampleID" Ref.fa SampleID.R1.fq.gz SampleID.R2.fq.gz  > SampleID.sam 
samtools sort -o SampleID.bam SampleID.sam 
samtools index SampleID.bam 
samtools flagstat SampleID.bam > output.infor # obtain mapping information
samtools depth SampleID.bam | wc -l >> output.infor # obtain coverage information
samtools depth SampleID.bam | awk '{sum+=$3} END {print sum/NR}' >> output.infor # obtain depth information
gatk MarkDuplicates -I SampleID.bam -O SampleID.sorted.markdup.bam -M SampleID.markdup.metrics.txt # mark duplication 
samtools index SampleID.sorted.markdup.bam
gatk HaplotypeCaller -R Ref.fa --sample-ploidy 2 --emit-ref-confidence GVCF -I SampleID.sorted.markdup.bam -O SampleID.sample.gvcf
bgzip -f SampleID.sample.gvcf # compress the gvcf file.
tabix -f -p vcf SampleID.sample.gvcf.gz # create index file for compressed gvcf file.
```

### Step3, Joint calling

```
for i in {01..12}
gatk GenomicsDBImport -R Ref.fa -L Chr$i --sample-name-map gvcf.path --genomicsdb-workspace-path Chr$i.db # All the gvcf file with absolute path were stored in gvcf.path.
```

### Step4, SNP and indel filtering

```
gatk SelectVariants -select-type SNP -V Chr$i.combined.vcf -O Chr$i.snp.vcf.gz
gatk VariantFiltration -V Chr$i.snp.vcf.gz --filter-expression "QD < 2.0" --filter-name "LowQD" --filter-expression "MQ < 40.0" --filter-name "MQ40.0" --filter-expression "FS > 60.0" --filter-name "FS60.0" --filter-expression "SOR > 3.0" --filter-name "SOR3.0" --filter-expression "MQRankSum < -12.5" --filter-name "MQRankSum-12.5" --filter-expression "ReadPosRankSum < -8.0" --filter-name "ReadPosRankSum-8.0" -O Chr$i.filter.snp.vcf.gz

gatk SelectVariants -select-type INDEL -V Chr$i.combined.vcf -O Chr$i.indel.vcf.gz
gatk VariantFiltration -V Chr$i.indel.vcf.gz --filter-expression "QD < 2.0" --filter-name "LowQD" --filter-expression "MQ < 40.0" --filter-name "MQ40.0" --filter-expression "FS > 200.0" --filter-name "FS200" --filter-expression "SOR > 10.0" --filter-name "SOR10" --filter-expression "MQRankSum < -12.5" --filter-name "MQRankSum-12.5" --filter-expression "ReadPosRankSum < -8.0" --filter-name "ReadPosRankSum-8.0" -O Chr$i.filter.indel.vcf.gz
```

### Step5, filtering variations located in TE region

```

```
