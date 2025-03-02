import gzip
import mcb185
import sys
import sequence

def find_orfs(dna, min_len=100):
    # Find ORFs in a DNA sequence
    orfs = []
    for frame in range(3):
        for strand in ['+', '-']:
            if strand == '-':
                dna = sequence.revcomp(dna)
            protein = mcb185.translate(dna[frame:])
            start_positions = []
            for i in range(len(protein)):
                if protein[i:i + 1] == 'M':
                    start_positions.append(i)

            for start in start_positions:
                for end in range(start + min_len, len(protein)):
                    if protein[end:end + 1] == '*':
                        orf = protein[start:end + 1]  
                        orf = orf.replace('*', '') + '*'  # replaces the * in the original codon files
                        orfs.append(orf)
                        break
    return orfs


min_len = int(sys.argv[2])

with gzip.open(sys.argv[1], 'rt') as f:
    seq = ''
    header = ''
    orf_count = 0  
    for line in f:
        if line.startswith('>'):
            if seq:
                orfs = find_orfs(seq, min_len)
                for orf in orfs:
                    print(f'>{header}-prot-{orf_count}')  # output format
                    print(orf)
                    orf_count += 1
            header = line.strip()[1:].split()[0]  # Extract only the NC_.. number
            seq = ''
        else:
            seq += line.strip()
    if seq:
        orfs = find_orfs(seq, min_len)
        for orf in orfs:
            print(f'>{header}-prot-{orf_count}')
            print(orf)
            orf_count += 1