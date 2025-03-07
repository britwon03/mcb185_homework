import sequence 
import sys 
import mcb185
def find_orfs(seq, min_len):
    orfs = []
    for frame in range(3):
        for strand_seq in [seq, sequence.revcomp(seq)]:
            protein = mcb185.translate(strand_seq[frame:])
            start = None
            for i, aa in enumerate(protein):
                if aa == 'M' and start is None:
                    start = i  # Mark the start of an ORF
                elif aa == '*' and start is not None and (i - start) >= min_len:
                    orfs.append(protein[start:i + 1])
                    start = None  # Reset start after finding a stop codon
    return orfs

min_len = int(sys.argv[2])
orf_count = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    orfs = find_orfs(seq, min_len)
    for orf in orfs:
        print(f'>{defline}-prot-{orf_count}')
        print(orf)
        orf_count += 1