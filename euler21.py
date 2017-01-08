#Project Euler Question 21
#Rachel Nash
#Amicable Numbers
#Answer: 31626
"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a not equal to b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""
def divisor_sum(n):
    divisors = []
    limit = n**0.5
    for x in range(1,int(limit)):
        if n%float(x)==0:
            divisors.append(x)
            if x!=1:
                divisors.append(n/x)
    if limit==int(limit):           #square numbers
        divisors.append(limit)
    return sum(divisors)

sumsofdivisors = [0]
amicable=[]
test = range(1,10000)
for num in test:
    d = divisor_sum(num)
    if num in sumsofdivisors:   #test for amicable
        a = sumsofdivisors.index(num)
        if a!=d:
            sumsofdivisors[a]=0
            if num in sumsofdivisors:
                a = sumsofdivisors.index(num)
        if d==a:
            amicable.append(num)
            amicable.append(a)
    sumsofdivisors.append(d)

print sum(amicable)

        
    
        
        