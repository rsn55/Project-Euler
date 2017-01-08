#Project Euler Question 23
#Rachel Nash
#Non-Abundant Sums
#Answer: 4179871
"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two
abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
def is_abundant(n):
    sum=0
    limit = n**0.5
    test=1
    while test<limit:
        if n%float(test)==0:
            sum+=test
            if test!=1:
                sum+=(n/test)
        test+=1
    if limit==int(limit):           #square numbers
        sum+=limit
    return sum>n

sum = 0
abundants = []
check = 0

for x in range(2,28123):
    if is_abundant(x):
        abundants.append(x)

for x in range(1,28123):
    for y in abundants:
        if (x-y >0) and ((x-y) in abundants):
            check = 1
            break
    if check==0:
        sum+=x
    else:
        check=0
print sum
