s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2) 

print('hey "dude" don\'t tell me what to do')
print(s1.count('h'))
# String Method 
print(s.upper()) 
print(s) 

print(s.replace('o', ' '))
print(s.replace('o', ' ').replace('r', 'i').replace('l', 'w'))

# list you can change [], but tuples and strings you can;'t 
import math 
# String Formatting 
print(f'{math.pi}') # prints pi 
print(f'{math.pi:.3f}') # prints pi with 3 fixed digits 
print(f'{1e6 * math.pi:e}') # exponential notation 
print(f'{"hello world":>20}') # right justify with space filler 
print(f'{"hello world":.>20}') # right justify with dot fillers 
print(f'{20:<10} {10}') #left justify 

print('{} {:.3f}'.format('str.format', math.pi))
print('%s %.3f' % ('printf', math.pi))

# Indexes 
seq = 'GAATTC'
print(seq[0],seq[1])
print(seq[-1])


for nt in seq: 
    print(nt, end = '')
print() 


for i in range(len(seq)): 
    print(i,seq[i])

# Slices 

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])

print(s[0:5], s[:5])        # both ABCDE
print(s[5:len(s)], s[5:])   # both FGHIJ

print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0,len(dna), 3): 
    codon = dna[i:i+3]
    print(i,codon)

# Tuples 
tax = ('Homo', 'sapiens', 9606) # Tuples are containers that holds multiple values using () 
print(tax) 

# Generates error because strings and tuples are immutable
'''
s[0] = 'C'
tax[0] = 'human'
'''

print(tax[0])
print(tax[::1])
 

# enumerate and zip
nts = 'ACGT'
for i in range(len(nts)): 
    print(i, nts[i])

for i, nt in enumerate(nts): # does the same thing as above
    print(i, nt) 

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)): 
    print(nts[i], names[i])

for nt, name in zip(nts, names): 
    print(nt, name)

for i, (nt, names) in enumerate(zip(nts, names)): 
    print(i, nt, name) 

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts) 

nts.append('C')
print(nts)

last = nts.pop() 
print(last) # prints the element that was removed 
print(nts)

nts.sort() 
print(nts) 
nts.sort(reverse =True)
print(nts) 

nucleotides = nts
nucleotides.append('C')
nucleotides.sort() 
print(nts, nucleotides)

# list()
items = list() 
print(items)
items.append('eggs')
print(items) 

stuff = [] 
stuff.append(3) 
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQERSER' 
print(alph)
aas = list(alph)
print(aas)

text = 'good day          to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# Searching 
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
'''
print('index Z?', alph.index('Z')) # returns an error 
'''

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z')) # returns a -1 bc not found


# Practice Problems 
def minimum(vals): 
    mini = vals[0]
    for val in vals[1:]: 
        if val < mini: mini = val 
    return mini 

vals = (3,4, 1, 2)
print(minimum(vals))

def minimax(vals): 
    maxi = vals[0]
    mini = vals[0] 
    for val in vals[1:]: 
        if val < mini : mini = val
        if val > maxi : maxi = val 
    return mini, maxi 

print(minimax(vals))


def mean(vals): 
    total = 0 
    for val in vals[0:]: 
        total += val 
    return (total/len(vals))

print(mean(vals))

import math 
def entropy(probs):
    h = 0
    for p in probs:
        if p > 0:
            h -= p * math.log2(p)
    return h

print(entropy([0.0, 0.3, 0.5]))


def dkl(P, Q): 
    d = 0 
    for p, q in zip(P,Q): # zips retrieves an element from each container
        d += p * math.log2(p/q) 
    return d 

p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)

print(dkl(p1, p2)) 

# command line data 

import sys 
print(sys.argv) 


# Coverting Types 

i = int('42')
x = float('0.61803')
print(i * x) 

x = float('hello')


# Pairwise Comparison 
for i in range(0,len(list)): 
    for j in range(X, len(list)):


    

