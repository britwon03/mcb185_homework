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
def tempconv(t): 5/9(t-32)

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
def distance(a, b): (a+ b)/2

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
