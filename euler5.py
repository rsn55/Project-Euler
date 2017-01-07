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


