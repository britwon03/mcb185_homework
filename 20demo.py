# Tuple --> collection of values separated by a comma. 
t = 1, 2 
print(t) 
print(type(t))

person = 'Steve', 21, 57891.50 
print(person)

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y #a function can return a tuple 

print(midpoint(2,3,4,5))


print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

print(m[0], m[1])

# Iteration 
i = 0 
while True: 
   i = i + 1 
   print ('hey', i) 
   if i == 3: break 

# condition loop 
i = 0 
while i < 10: 
    print(i) 
    i = i + 3 
print('final value of is', i)

# for i in range()
for i in range(1,10,3): 
    print(i) 

for i in range(0,5): 
    print(i) 

for i in range(5): 
    print(i) 

basket = 'milk', 'eggs', 'bread'
for thing in basket: 
    print(thing)

for i in range(len(basket)): 
    print (basket[i])

# Nesting 
for i in range(7): 
    if i % 2 == 0: print(i, 'is even')
    else:           print(i, 'is odd') 


#Practice Problems
# triangle numbers 
def triangular(n): 
    triangle = 0
    for i in range(1,n + 1): 
        print ('add', i, 'to total')
        triangle = triangle + i 
    return triangle 

print(triangular(2))

# Factorial
def factorial(n): 
    if n == 0 or n == 1: return 1 
    result = 1 
    for i in range (1, n + 1): 
        result = result * i 
    return result

print(factorial(4))

# poisson distribution 
import math 
def poisson(n, k): 
    return n**k * math.e**-n /factorial(k) 

print(poisson(1,2))

# n choose k 
def nchoosek(n, k): 
    return factorial(n) /  (factorial(k) * factorial((n-k)))

print(nchoosek(1,2))

# Euler's number: 
def euler(limit): 
    e = 0 
    for n in range(limit): 
        e = e + 1 / factorial(n)
    return e 

print(euler(3))

# Prime Number 
def is_prime(n):
    for den in range(2, n//2):
        if n % den == 0: return False
    return True


print(is_prime(2)) 
print(is_prime(4)) 

# Nilakantha series 
def nilakantha(limit): 
    pi = 3 
    for i in range(1,limit + 1): 
        n = 2 * i 
        d = n * (n + 1) * (n + 2)
        if i % 2 == 0: pi = pi - 4 / d 
        else:          pi = pi + 4 / d 
    return pi 


# Random Numbers
import random
for i in range(5): 
    print(random.random())

for i in range(3): 
    print(random.randint(1,6)) 

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

# More Practice
# Monty Pi-thon 
import random 
inside_circle = 0
total_points = 0 
while True: 
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    distance = x**2 + y**2 
    if distance <= 1: 
        inside_circle += 1 
        total_points += 1 
    pi_estimate = (inside_circle / total_points) * 4 
    print(pi_estimate)

    if total_points <= 10: break 

# D&D Stats
import random
trials = 100


sum_3D6 = 0
sum_3D6r1 = 0
sum_3D6x2 = 0
sum_4D6d1 = 0

# Perform trials using a while loop
i = 0
while i < trials:
    # 3D6: Roll 3 six-sided dice
    total = 0
    for i in range(3):
        total += random.randint(1, 6)
    sum_3D6 += total

    # 3D6r1: Roll 3 six-sided dice, but re-roll 1s
    total = 0
    for i in range(3):
        roll = random.randint(1, 6)
        if roll == 1:
            roll = random.randint(2, 6)  
        total += roll
    sum_3D6r1 += total

    # 3D6x2: Roll pairs of dice 3 times, keeping the max each time
    total = 0
    for i in range(3):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total += max(roll1, roll2)  
    sum_3D6x2 += total

    # 4D6d1: Roll 4 dice, drop the lowest
    rolls = []
    for i in range(4):
        rolls.append(random.randint(1, 6))
    rolls.sort() 
    total = sum(rolls[1:]) 
    sum_4D6d1 += total

    i += 1  # Increment counter for while loop

# Compute averages
avg_3D6 = sum_3D6 / trials
avg_3D6r1 = sum_3D6r1 / trials
avg_3D6x2 = sum_3D6x2 / trials
avg_4D6d1 = sum_4D6d1 / trials

print(avg_3D6)
print(avg_3D6r1)
print(avg_3D6x2)
print(avg_4D6d1)








 