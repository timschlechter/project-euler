# https://en.wikipedia.org/wiki/Combination
# https://www.youtube.com/watch?v=Ul4nl1S968E
# https://www.mathblog.dk/project-euler-15/

# 40 moves of which 20 must be down (D), and 20 must be right (R)

# We have a N*N grid
# all paths have size 2N, which will contain N down and N right
# we have 2N objects. If we place all N down moves, the N right moves are given

from math import factorial

def C(n, k):
    return factorial(n) / (factorial(k) *  factorial(n-k))

N = 20
n = 2*N
k = N

print(C(n, k))
