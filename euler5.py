#Project Euler Question 5
#Rachel Nash
#Smallest Multiple
#Answer: 232792560

"""2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder. What is the smallest
positive number that is evenly divisible by all of the numbers from 1 to 20?"""
numbers = range(1,21)
product=1
for num in numbers:
    if product%float(num)==0:
        pass
    elif num in [4,8,9,16]:
        if product%(num/2.0)==0:
            product*=2
        elif product%(num/3.0)==0:
            product*=3
    else:
        product*=num
print product






"""def primesinto(num):
    primes = []
    composites = []
    for int in range(2,num+1):
        if not int in composites:
            primes.append(int)
            for x in range(int*2,num+1, int):
                composites.append(x)
    factors = []
    for i in primes:
        if num%i ==0:
            factors.append(i)
    return factors
    

check = range(2,21)
product = 1
for x in check:
    print x
    if x<product:
        remain = product%x
    else:
        remain=x/product
    facts = primesinto(x)

    if remain !=0:
        if remain != 1:
            if remain in facts:
                product*=remain
            elif x/float(remain) in facts:
                product*=remain
            elif x/float(remain)/float(remain) in facts:
                product*=remain

        else:

            product *= x
    print str(int(product))+"is product"
    print 'next'
    
print int(product)"""


