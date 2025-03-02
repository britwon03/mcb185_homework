import math 
import sys 
import gzip 


# Shannon Entropy Calculation 
def shannon_entropy(seq):
    total = len(seq)
    if total == 0:
        return 0
    frequencies = []
    for nuc in "ACGT":
        count = seq.count(nuc)
        if count > 0:
            frequencies.append(count / total)
    entropy = 0
    for p in frequencies:
        entropy -= p * math.log2(p)
    return entropy

# Checks and masks low complexity regions 
def mask_low_complexity(seq, window, threshold):
    masked_seq = list(seq)
    for i in range(len(seq) - window + 1):
        window_seq = seq[i:i+window]
        entropy = shannon_entropy(window_seq) # compares window to entropy threshold
        if entropy < threshold:
            for j in range(i, i+window):
                masked_seq[j] = 'N'
    return ''.join(masked_seq)


# fix this 
window = int(sys.argv[2])
threshold = float(sys.argv[3])
with gzip.open(sys.argv[1], 'rt') as fp: 
    header = None 
    sequence = [] 
    for line in fp: 
        line = line.strip() 
        if line.startswith('>'): # first line of file 
            if header: 
                print(header) 
                masked_seq = mask_low_complexity(''.join(sequence), window, threshold) 
                for i in range(0, len(masked_seq), 60): 
                    print((masked_seq[i:i+60]))
            header = line 
            sequence = [] 
        else: 
            sequence.append(line) 
    if header: # continues on with each line of the sequence 
        print(header)
        masked_seq = mask_low_complexity(''.join(sequence), window, threshold)
        for i in range(0, len(masked_seq), 60):
            print(masked_seq[i:i+60])

