# SNP fingerprints of cauliflower
CoreSNPSimulation.py
Select a core SNP set for variety identification.
First, a certain number of SNPs were randomly extracted from chromosomes for 5,000 times. Then, the discernibility of each set of SNPs were evaluated in the core germplasm of cultivars. Only the set of SNPs which could distinguish the maximum number of cauliflower cultivars were selected as candidate SNP loci.

usage:
```
python3 CoreSNPSimulation.py file_marker.geno core_samples.txt marker_number(int) times(int)
```
