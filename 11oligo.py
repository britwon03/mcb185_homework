def tm(a, c, g, t): 
    if a + c + g + t <= 13: return ((a +t)**2 + (g + c) **4)
    return 64.9 + 41* (g + c -16.4) / (a + t + g +c)

print(tm(5,7,3,4))
print(tm(2,5,4,1))
print(tm(13, 25, 18, 27))
print(tm(4, 6, 7, 8))

