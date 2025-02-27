import sys 
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]): 
    defwords = defline.split() 
    name = defwords[0]
    print(name, end = ' ')
    for nt in 'ACGTN': 
        print(seq.count(nt) / len(seq), end = ' ')
    print()