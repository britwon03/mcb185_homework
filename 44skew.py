import sys
import gzip
import sequence  

w = int(sys.argv[2])


seq = ""
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if not line.startswith('>'):
            seq += line.strip()

# Initialize GC count for the first window
g_count = seq[:w].count('G')
c_count = seq[:w].count('C')

# Compute GC composition and skew for the first window 
gc_comp = sequence.gc_comp(seq[:w])  
gc_skew = sequence.gc_skew(seq[:w])    
print(0, gc_comp, gc_skew)

# Slide the window across the sequence
for i in range(1, len(seq) - w + 1):
    left_nt = seq[i - 1]   # Leaving nucleotide
    right_nt = seq[i + w - 1]  # Incoming nucleotide

    # Update GC counts 
    g_count += (right_nt == 'G') - (left_nt == 'G')
    c_count += (right_nt == 'C') - (left_nt == 'C')

    
    window_seq = seq[i:i + w]  # Extract the current window
    gc_comp = sequence.gc_comp(window_seq)  
    gc_skew = sequence.gc_skew(window_seq)    

    print(i, gc_comp, gc_skew)







