import sys
import gzip

kd_values = {
    'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
    'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
    'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
    'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

def kd(seq):
    # Calculate KD score for a sequence
    if len(seq) == 0: 
        return 0 
    total_kd = 0
    for aa in seq:
        if aa in kd_values:
            total_kd += kd_values[aa]
    return total_kd / len(seq)

# Process FASTA file
with gzip.open(sys.argv[1], 'rt') as fp:
    header = ''
    protein = ''
    
    for line in fp:
        if line.startswith('>'):
            if protein:
                sp = False
                tm = False
                
                # Check for signal peptide
                for i in range(0, 30 - 7): # first 30 aa with 8 aa long 
                    region = protein[i:i + 8]
                    if kd(region) >= 2.5 and 'P' not in region:
                        sp = True
                        break

                # Check for transmembrane region
                for i in range(30, len(protein) - 10):
                    region = protein[i:i + 11]
                    if kd(region) >= 2.0 and 'P' not in region: # makes sure Proline is not in region 
                        tm = True
                        break

                # If both conditions are met, print the protein header
                if sp and tm:
                    print(header[:60])

            header = line.strip()[1:]
            protein = ''
        else:
            protein += line.strip()
