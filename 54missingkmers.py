import sys
import itertools
import mcb185
import sequence


sequences = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    sequences.append(seq)
    sequences.append(sequence.revcomp(seq))  # both strands of the sequence

k = 1
while True:
    kcount = {}
    for seq in sequences:
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i + k]
            if kmer not in kcount:
                kcount[kmer] = 0
            kcount[kmer] += 1
    
    missing_kmers = []
    for nts in itertools.product('ACGT', repeat=k):
        kmer = ''.join(nts)
        if kmer not in kcount:
            missing_kmers.append(kmer)
    
    if missing_kmers:
        print(f"Missing k-mers found at k={k}:")
        for kmer in missing_kmers:
            print(kmer)
        break
    
    k += 1
