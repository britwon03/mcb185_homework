
# prime number 
def is_prime(n): 
    for i in range(2, n//2 + 1): 
        if n % i == 0: return False 
    return True 

print(is_prime(4))
print(is_prime(13))

for i in range(51, 0, -2): 
    if is_prime(i) == True: print(i,'*', sep='')
    else: print(i) 




# attempted to do the parabola example 
import random 

points_below = 0 
points_above = 0 

while True: 
    x = random.randint(1,100) 
    d = x ** 2 
    if d > 1: points_above += 1 
    else: points_below += 1 
    print(points_below/points_above)