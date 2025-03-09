import sys
import gzip
import sequence  

w = int(sys.argv[2])

# Read sequence from gzipped FASTA file
seq_list = []
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line.startswith('>'):
            continue
        seq_list.append(line.strip())

seq = "".join(seq_list)

# Initialize GC count and GC skew
G_count = seq[:w].count('G')
C_count = seq[:w].count('C')

# Compute GC composition and GC skew for first window
gc_comp = (G_count + C_count) / w
if (G_count + C_count) > 0: # avoids division by 0 
    gc_skew = (G_count - C_count) / (G_count + C_count)
else:
    gc_skew = 0 
print(0, gc_comp, gc_skew)

# Slide the window across the sequence
for i in range(1, len(seq) - w + 1):
    left_nt = seq[i - 1]   # Leaving nucleotide
    right_nt = seq[i + w - 1]  # Incoming nucleotide
    
    # Update counts
    if left_nt == 'G': G_count -= 1
    if left_nt == 'C': C_count -= 1
    if right_nt == 'G': G_count += 1
    if right_nt == 'C': C_count += 1






