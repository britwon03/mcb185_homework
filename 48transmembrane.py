import sys
import gzip
kd_values = {
    'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
    'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
    'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
    'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

def kd(seq):
   # Calculates the average Kyte-Doolittle hydrophobicity for a sequence.
    total_kd = 0
    for aa in seq:
        if aa in kd_values:  # Only add if the amino acid is valid
            total_kd += kd_values[aa]
        else:
            total_kd += 0  # Treat unknown amino acids as 0
    return total_kd / len(seq) if seq else 0

def signal_peptide(protein):
   # Checks for a hydrophobic signal peptide in the first 30 amino acids.
    if len(protein) < 30:
        return False
    for i in range(0, 30 - 7):  # Sliding window across first 30 aa
        region = protein[i:i+8]
        if kd(region) >= 2.5 and 'P' not in region:
            return True
    return False

def transmembrane_region(protein):
    # Checks for a transmembrane region beyond the first 30 amino acids.
    for i in range(30, len(protein) - 10):
        region = protein[i:i+11]
        if kd(region) >= 2.0 and 'P' not in region:
            return True
    return False

def is_transmembrane(protein):
    #Determines if a protein is transmembrane.
    return signal_peptide(protein) and transmembrane_region(protein)

# Process FASTA file
with gzip.open(sys.argv[1], 'rt') as fp:
    header = ''
    protein = ''
    
    for line in fp:
        if line.startswith('>'):
            if protein and is_transmembrane(protein):
                print(header[:60])  # Truncate to match example output
            header = line.strip()[1:]  # Remove '>'
            protein = ''
        else:
            protein += line.strip()
    
    # Process last sequence
    if protein and is_transmembrane(protein):
        print(header[:60])
