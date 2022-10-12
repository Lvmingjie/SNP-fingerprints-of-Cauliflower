# Author Lvmin
# coding=utf-8
# @Time    : 2022/1/9 21:53
# @File    : genotype_to_vcf.py
# @contact: lvmingjie_good@163.com
# !/usr/bin/env python
import sys

###header#############

file = sys.argv[1]
fot = open(sys.argv[1][:-3]+"vcf", 'w')
fot.write('##fileformat=VCFv4.2\n'
          '##ALT=<ID=NON_REF,Description="Represents any possible alternative allele not already represented at this location by REF and ALT">\n'
          '##FILTER=<ID=LowQual,Description="Low quality">\n'
          '##FORMAT=<ID=AD,Number=R,Type=Integer,Description="Allelic depths for the ref and alt alleles in the order listed">\n'
          '##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Approximate read depth (reads with MQ=255 or with bad mates are filtered)">\n'
          '##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">\n'
          '##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">\n'
          '##FORMAT=<ID=PL,Number=G,Type=Integer,Description="Normalized, Phred-scaled likelihoods for genotypes as defined in the VCF specification">\n'
          '##INFO=<ID=AC,Number=A,Type=Integer,Description="Allele count in genotypes, for each ALT allele, in the same order as listed">\n'
          '##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency, for each ALT allele, in the same order as listed">\n'
          '##INFO=<ID=AN,Number=1,Type=Integer,Description="Total number of alleles in called genotypes">\n'
          )

fai = "/aglab200T/aglab/cr/3_genomes/Cauliflower/6_rename_genome_2020Jul15/Cauliflower_genome.fasta.fai"
fin_fai = open(fai, 'r')
for line in fin_fai:
    _line = line.split("\t")
    fot.write("##contig=<ID=%s,length=%s>\n" %(_line[0], _line[1]))
fot.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t")

####Genotype
fin = open(file, 'r')
ti = fin.readline().strip("\n")
samples = ti.split("\t")[5:]
fot.write("\t".join(samples)+"\n")
for line in fin:
    line = line.rstrip()
    _line = line.split("\t")
    chrom = _line[1]
    pos = _line[2]
    ref = _line[3]
    alt = _line[4]
    fot.write("%s\t%s\t.\t%s\t%s\t1000\t.\t.\tGT:AD:DP:GQ:PL" %(chrom, pos, ref, alt))  #AD=0,100, GQ=60, PL="."
    for i in range(len(samples)):
        if _line[i+5].split(":")[0] == _line[i+5].split(":")[1] and _line[i+5].split(":")[0] == ref:
            fot.write("\t"+"0/0:100,0:100:60:.")
        elif _line[i+5].split(":")[0] == _line[i+5].split(":")[1] and _line[i+5].split(":")[0]== alt:
            fot.write("\t"+"1/1:0,100:100:60:.")
        elif _line[i+5].split(":")[0] == "-" or _line[i+5].split(":")[1] == "-":
            fot.write("\t"+"./.:0,0:0:0:0")
        else:
            fot.write("\t"+"0/1:50,50:100:60:.")
    fot.write("\n")
