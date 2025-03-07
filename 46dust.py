import sys
import math
import mcb185

def entropy(win):
    a = win.count('A') / len(win)
    c = win.count('C') / len(win)
    g = win.count('G') / len(win)
    t = win.count('T') / len(win)
    h = 0
    for freq in [a, c, g, t]:
        if freq > 0:
            h += freq * math.log2(freq)
    return -h

window_size = int(sys.argv[2]) 
entro_threshold = float(sys.argv[3])



for defline, seq in mcb185.read_fasta(sys.argv[1]): 
    mask = list(seq) 
    for i in range(len(seq) - window_size + 1): 
        win = seq[i: i + window_size]
        if entropy(win) < entro_threshold: 
            for j in range(i, i + window_size): 
                mask[j] = 'N'
    
    print(defline) 
    masked_seq = ''.join(mask) 
    for i in range(0, len(masked_seq), 60): 
        print(masked_seq[i: i + 60])


