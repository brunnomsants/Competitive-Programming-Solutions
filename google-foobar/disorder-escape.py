from math import factorial
from collections import Counter
from fractions import gcd

def solution(w, h, s):
    grid=0   #using the cycle_partitions, solution calculates the grid count by considering all possible pattern configurations for the width and height of the grid
    for lw in cycle_partitions(w):
        for lh in cycle_partitions(h):            
            a=cycle_count(lw, w)*cycle_count(lh, h)
            grid+=a*(s**sum([sum([gcd(i, j) for i in lw]) for j in lh]))
              
    return str(grid//(factorial(w)*factorial(h)))
def cycle_count(c, n):
    cc=factorial(n)
    for a, b in Counter(c).items(): # Divide count variable by (a**b)*factorial(b) for each number count
        cc//=(a**b)*factorial(b)
        # Return the count variable as the final cycle count
    return cc        
def cycle_partitions(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for p in cycle_partitions(n-i, i):
            yield [i] + p
            #This algorithm works by exploring all possible cycle partitions, 
            #with the aim of finding partitions that form cycles with all positive 
            #integers less than or equal to n.