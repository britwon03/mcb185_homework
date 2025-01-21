# Task 1 
zless ~/Code/MCB185/data/A.thaliana.gff.gz | cut -f 7 | sort | uniq -c 

# Task 2 
gunzip -c Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz | grep "reductase" | uniq -c | cut -f 10 | sort | uniq -c  
 177 
 gunzip -c Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz | grep "transporter" | uniq -c | cut -f 10 | sort | uniq -c 
 293 



# Task 3 

zless Code/MCB185/data/jaspar2024_core.transfac.gz | grep "tax_group" | sort | uniq -c         