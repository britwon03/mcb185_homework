def is_prime(n): 
    for i in range(2,n//2 +1): 
        if n % i == 0: return False 
        return True 

print(is_prime(4))

for n in reversed(range(1,53,2)): 
    if is_prime(n) == True:
        print(n, "*") 
    else: print(n) 







    