import sys
import math

def is_palindrome(x):
    c = list(str(x))
    l = len(c)
    if l % 2 == 1:
        return False
    for i in range(0, int(l/2)):
        if c[i] != c[l-i-1]:
            return False    
    return True

m = 0
for x in reversed(range(317, 1000)):
    for y in reversed(range(317, 1000)):
        if (is_palindrome(x*y)):
            m = max(m, x*y)
            
print(m)
      

