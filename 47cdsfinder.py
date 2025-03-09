import sys
import mcb185
import sequence

min_len = int(sys.argv[2])
orf_count = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for strand_seq in [seq, sequence.revcomp(seq)]:  # Both DNA strands
        for frame in range(3):  # Three reading frames
            protein = mcb185.translate(strand_seq[frame:])
            start = None
            
            for i, aa in enumerate(protein):
                if aa == 'M' and start is None:
                    start = i  # Start of ORF
                elif aa == '*' and start is not None:
                    orf_seq = protein[start:i]  # Exclude stop codon (*)

                    if len(orf_seq) >= min_len:  
                        print(f'>{defline}-prot-{orf_count}')
                        print(orf_seq)  # Print ORF sequence
                        orf_count += 1
                    
                    start = None  # Reset for next ORF