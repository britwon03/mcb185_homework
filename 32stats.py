import math 
import sys 
vals = [float(x) for x in sys.argv[1:]]
def minimum(vals): 
    mini = vals[0]
    for val in vals[1:]: 
        if val < mini: mini = val
    return mini 

def maximum(vals): 
    maxi = vals[0]
    for val in vals[1:]: 
        if val > maxi: maxi = val
    return maxi 

def mean(vals): 
    total = 0 
    for val in vals[0:]: 
        total += val
    return (total/ len(vals))

def stdv(vals): 
    if len(vals) < 2: 
        return 0 
    avg = mean(vals) 
    variance = 0
    for val in vals:
        variance += (val - avg) ** 2
    variance /= (len(vals) - 1)
    return math.sqrt(variance)

def median(vals):
    sorted_num = sorted(vals)
    n= len(sorted_num)
    mid = n//2 
    if n % 2 == 0: 
        return (sorted_num[mid - 1] + sorted_num[mid])/2  
    else: 
        return sorted_num[mid]



print(f'Number of Values: {len(vals)}') 
print(f'Mean: {mean(vals)}')
print(f'Minimum: {minimum(vals)}')
print(f'Maximum: {maximum(vals)}')
print(f'Median: {median(vals)}')
print(f'Standard Deviation: {stdv(vals)}')