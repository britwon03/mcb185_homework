
letters = 'ACGTNQW'
# print header 
print(end = '  ')
for letter in letters: 
    print(letter, end = ' ')
print() # header line needs to end 
# print matrix
for c1 in letters: 
    print(c1, end = ' ')
    for c2 in letters: 
        if c1 == c2: 
            print('+', end = ' ')
        else: 
            print('-', end = ' ')
    print()

