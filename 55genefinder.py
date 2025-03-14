import sys
import mcb185
import sequence

min_len = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    seqid = defline.split()[0]
    gff_entries = []
    
    for strand, dna_seq in [('+', seq), ('-', sequence.revcomp(seq))]:
        for frame in range(3):
            protein = mcb185.translate(dna_seq[frame:])
            start = None
            
            i = 0
            while i < len(protein):
                if protein[i] == 'M' and start is None:
                    start = i
                elif protein[i] == '*' and start is not None:
                    orf_len = (i - start) * 3  # Convert from protein to DNA length
                    if orf_len >= min_len:
                        if strand == '+':
                            start_nt = frame + start * 3 + 1
                            end_nt = frame + i * 3 + 3
                        else:
                            start_nt = len(dna_seq) - (frame + i * 3 + 3) + 1
                            end_nt = len(dna_seq) - (frame + start * 3) + 1
                        
                        gff_entries.append(f"{seqid}\tCDS\t{start_nt}\t{end_nt}\t{strand}")
                    start = None
                i += 1
    
    for entry in gff_entries:
        print(entry)