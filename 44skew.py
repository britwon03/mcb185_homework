import sequence 
import gzip 
import sys 

w = int(sys.argv[2])

seq = ''
with gzip.open(sys.argv[1], 'rt') as fp: 
    for line in fp: 
        if not line.startswith('>'): 
            seq += line.strip() 

g_count = seq[:w].count('G')
c_count = seq[:w].count('C')

# inital gc count 

gc_count = sequence.gc_comp(seq[:w])
gc_skew = sequence.gc_skew(seq[:w])
print(0, gc_count, gc_skew)

# Sliding Window 
for i in range(0, len(seq) - w + 1): 
    left_nt = seq[i - 1]
    right_nt = seq[i + w - 1]

    g_count += (right_nt == 'G') - (left_nt == 'G') 
    c_count += (right_nt == 'C') - (left_nt == 'C')

    gc_comp = (g_count + c_count) / w 
    if (g_count + c_count) >0: 
        gc_skew = (g_count - c_count) / (g_count + c_count)
    else: 
        gc_skew =  0 
    print(i, gc_comp, gc_skew)







