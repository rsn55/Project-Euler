#Project Euler Question 7
#Rachel Nash
#10,001st Prime
#Answer:104743
import math
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10,001st prime number?"""
num=10001
primes = []
composites = []
estimate = 500000
int=2
while len(primes)<num:
    if not int in composites:
        primes.append(int)
        for x in range(int*2,estimate, int):
            composites.append(x)
    int+=1
print primes[-1]
