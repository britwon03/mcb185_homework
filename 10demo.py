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

