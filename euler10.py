#Project Euler Question 10
#Rachel Nash
#Summation of Primes
#Answer:142,913,828,922

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

limit=2000000
composites = []
int=2
sum=0
while int<limit:
    if not int in composites:
        sum+=int
        for x in range(int*2,limit, int):
            composites.append(x)
    int+=1
print sum
    