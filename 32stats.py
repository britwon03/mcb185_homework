import sys 
import math 



def minimax(vals): 
    maxi = vals[0]
    mini = vals[0] 
    for val in vals[1:]: 
        if val < mini : mini = val
        if val > maxi : maxi = val 
    return mini, maxi 

def mean(vals): 
    total = 0 
    for val in vals[0:]: 
        total += val 
    return (total/len(vals))

def stdv(vals): 
    if len(vals) < 2:
        return 0
    avg = mean(vals)
    variance = sum((x - avg) ** 2 for x in vals) / (len(vals) - 1)
    return math.sqrt(variance)

def median(vals):
    sorted_num = sorted(vals)
    n= len(sorted_num)
    mid = n//2 
    if n % 2 == 0: 
        return (sorted_num[mid - 1] + sorted_num[mid])/2  
    else: 
        return sorted_num[mid]


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 32stats.py num1 num2 num3 ...")
        return
    
    try:
        vals = list(map(float, sys.argv[1:]))
    except ValueError:
        print("Provide a list of numeric values.")
        return
    
    print(f'Number of values: {len(vals)}')
    print(f'Minimum value, Maximum Value: {minimax(vals)}')
    print(f'Mean: {mean(vals)}')
    print(f'Standard Deviation: {stdv(vals)}')
    print(f'Median: {median(vals)}')


main()