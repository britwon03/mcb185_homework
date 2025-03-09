s = {'A', 'C', 'G'}
s.add('T')
s.add('A') # bc its a set, adding the same element will not do anything
print(s)
# print(s[2])  --> will print out error bc theres no order 

# Dictionaries 
d = {'dog': 'woof', 'cat': 'meow'}
print(d['cat'])
d['pig'] = 'oink'
d['cat'] = 'mew'
del d['cat']
if 'dog' in d: print(d['dog'])

# Iterations 
for key in d: print(f'{key} says {d[key]}') # does the same thing 
for k, v in d.items(): print(k, 'says', v) # does the same thing 
for thing in d.items(): print(thing[0], thing[1]) 
print(d.keys(), d.values(), list(d.values()))

# Lookup tables 
# cleaner look
kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)
'''
# Categorical Data 
    for k, v in sorted(count.items(), key=lambda item: item[1]):
        print(k, v) # count needs to be a list a things 

def by_value(tuple):
    return tuple[1]

for k, v in sorted(count.items(), key=by_value):
    print(k, v)
'''

# K - mers 
import itertools
for nts in itertools.product('ACGT', repeat=2):
    print(nts)


# Argparse 

# Positional Arguments 


