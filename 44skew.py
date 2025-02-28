import sequence
import sys 
import gzip 
fasta_file = sys.argv[1]
window_size = int(sys.argv[2])
## Fast Algorithm: 
# Read sequence properly
seq_list = [] # changing from string = faster running time 
with gzip.open(fasta_file, 'rt') as fp:
    for line in fp:
        if line.startswith('>'):
            continue
        seq_list.append(line.strip()) 
seq = "".join(seq_list)  # Convert list to a single string (efficient concatenation)
for i in range(len(seq) - window_size + 1):
    window_seq = seq[i:i + window_size]
    gc_cont = sequence.gc_comp(window_seq)
    gc_skewval = sequence.gc_skew(window_seq)
    print(i, gc_cont, gc_skewval)



# Slow Algorithm: mainly due to adding sequence to string
import sys 
import gzip 
fasta_file = sys.argv[1]
window_size = int(sys.argv[2])

# Read sequence properly
seq = ""
with gzip.open(fasta_file, 'rt') as fp:
    for line in fp:
        if line.startswith('>'):
            continue
        seq += line.strip() 
 # Concatenate sequence lines + places it in the string to create a long DNA sequence
for i in range(len(seq) - window_size + 1):
    window_seq = seq[i:i + window_size]
    gc_content = sequence.gc_comp(window_seq)
    gc_skew_val = sequence.gc_skew(window_seq)
    print(i, gc_content, gc_skew_val)