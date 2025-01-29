# Distance between two points in a graph 
import math 
def dist2pt(x1, y1, x2, y2): 
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(dist2pt(1,2,3,4))


# function that determines if its a valid probability 
def is_valid_prob(num): 
    return 0 <= num <= 1 

print(is_valid_prob(2.5)) 
print(is_valid_prob(0.4))


# function that returns the max 

def max_num4(a, b, c, d): 
  if a >= b and a >= c and a >=d: return a 
  elif b >= a and b >= c and b >= d: return b
  elif c >= a and c >= b and c >= d: return c 
  else: return d 

print(max_num4(2,3,4,5))

#function to return the min 
def min_num4(a, b, c, d): 
  if a <= b and a <= c and a <=d: return a 
  elif b <= a and b <= c and b <= d: return b 
  elif c <= a and c <= b and c <= d: return c 
  else: return d 

print(min_num4(2,3,4,5))

