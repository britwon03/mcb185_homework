# 10demo.py by Britney Ly 

print('hello, again') # greeting 

"""
This is a 
multi -line 
comment
"""

# math functions 
import math 
print(1.5e-2)
print(1+1)
print(1-1)
print(2*2)
print(1/2)
print(2**3)
print(5//2)
print(5 % 2)
print(5 * (2+1))
print(abs(-5))
print(pow(5,3))
print(round(1.22345, ndigits=3))
print(math.log2(4))
print(math.factorial(5))

print(0.1 * 1)
print(0.1 *3)

# Variables 
a = 3 
b = 4 
c = math.sqrt(a**2 + b**2)
print(c) 

# Type 
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ', end='!\n') # for separating the output

# Function 
def pythagoras( a,b): 
    c= math.sqrt(a**2 + b**2)
    return c 

hyp = pythagoras(3,4)
print(hyp)

# Simplifying 
def pythagoras(a,b): 
    return math.sqrt(a**2 + b**2)

print(pythagoras(3,4))
pythagoras(3,4) # this is not like R, if you don't use print() it would show you the output, it will still evaluate though.

# Block Structure 
def pythagoras(a,b): return math.sqrt(a**2 + b**2) # if there is only 1 statement in a block, you can omit the indent.


# Practice
def circle_area(r): math.pi * r**2
def rectangle_area(w,h): return w * h
def triangle_area(w,h): return rectangle_area(w,h) / 2

# Convert temp from F to C 
def tempconv(t): return (5/9) * (t-32)
print(tempconv(98.6))


# Speed Conversion 
def speed_conv(s): 1.60934 * s 

# DNA concentration 
def dna_conc(od260,dilution_factor): return od260 * dilution_factor * 50

# arithmetic mean
def arth_mean (a,b,c): return (a + b + c)/3
# geometric mean of 3 
def geo_mean(a,b,c): return (a * b * c) ** (1/3)

# harmonic mean of 3 
def harm_mean(a,b,c): return 3/((1/a) + (1/b) + (1/c)) 

# distance between 2 points in a graph 
def distance2(x1, y1, x2, y2): 
    x_dis = x2 -x1
    y_dis = y2 -y1
    return math.sqrt(x_dis ** 2 + y_dis ** 2)

print (distance2(1,2,3,4))


# Strings 

s = 'hello world'
print(s, type(s))

# Conditional 
a = 2 
b = 2
if a == b: 
    print ('a equal b')
    print(a,b)

def is_even(x): 
    if x % 2 == 0: return True 
    return False #similar to ifelse statement 
print(is_even(2))
print(is_even(3))

#Boolean 
c = a == b 
print(c) 
print(type(c))

# if - elif- else 
if a < b: 
    print('a < b')
elif a > b: 
    print('a > b')
else: 
    print ('a == b')

if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

if   a < b:  print('a < b')
elif a <= b: print('a <= b') # only first TRUE condition is executed 
elif a == b: print('this will never print!')

# Chaining 
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

# Floating Point Warning 
a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b') # bc they have infinite precision, NEVER TEST FOR equality with floating point num

#how to deal with floats 
print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')

#how python deals with it 
if math.isclose(a, b): print('close enough')

# String Comparison 
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a') # all lower cases have higher ASCII values than upper cases 

# Mismatch Type Error 
a = 1
s = 'G'
#if a < s: print('a < s') # 1 and G are different types, thus makes no sense to compare them 

# None Type 
def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4)) # None is printed bc no return in function 

# More Practice 
def is_integer(num): 
    return num % 1 == 0

print(is_integer(3)) 

def is_valid_prob(num): 
    return 0 <= num <= 1 

print(is_valid_prob(2.5)) 
print(is_valid_prob(0.4))

def molecular_weight(letter): 
    weights = {
        'A': 331.2,  # Adenine
        'T': 322.2,  # Thymine
        'C': 307.2,  # Cytosine
        'G': 347.2   # Guanine
    }
    return weights.get(letter.upper())

print(molecular_weight('A'))
print(molecular_weight('t'))
print(molecular_weight('C'))
print(molecular_weight('g'))
print(molecular_weight('B'))

def compl_letter(letter): 
    complement = { 
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return complement.get(letter.upper())

print(compl_letter('A'))
print(compl_letter('c'))
print(compl_letter('G'))
print(compl_letter('t'))
print(compl_letter('e'))


# Even more Practice 
def max_num(a, b, c): 
  if a >= b and a>= c: return a 
  elif b >= a and b >= c: return b
  else: return c 

print(max_num(2,3,4))
print(max_num(6,3,4))
print(max_num(2,9,5))

# Practice Problem 
def sensitivity(tp, fn): 
    """Calculate sensitivity""" 
    if tp + fn == 0: return None 
    return tp / (tp + fn) 

def specificity(tn, fp): 
    """ Calculate specificity""" 
    if tn + fp == 0 : return None 
    return tn / (tn + fp)

def f1_score(tp, fp, fn): 
    if tp + fp == 0: return None 
    precision = tp / (tp + fp)
    sensitivity = tp / (tp + fn) 
    if precision + sensitivity == 0 : return None 
    return 2 * (precision * sensitivity) / (precision + sensitivity)

tp = 50 
fp = 20 
tn = 100
fn = 25

print(sensitivity(tp, fn))
print (specificity(tn, fp))
print(f1_score(tp, fp, fn))

# Shannon Entropy 
import math 
def shannon_entropy (a, c, g, t): 
    total = a + c + g + t 
    if total == 0: return 0 
    
    probabilities = [a /total, c/total, g/total, t/total]
    # Entropy Calculation 
    entropy = -sum (p * math.log2(p) for p in probabilities if p > 0)
    return abs(entropy) 

print(shannon_entropy(10, 10, 10, 10)) 
print(shannon_entropy(40, 10, 5, 5))  
print(shannon_entropy(0, 0, 0, 0))     
print(shannon_entropy(50, 0, 0, 0)) 
