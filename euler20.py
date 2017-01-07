#Project Euler Question 20
#Rachel Nash
#Factorial Digit Sum
# Answer: 648

"""n! means n x (n - 1) x ... x 3 x 2 x 1
    For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    Find the sum of the digits in the number 100!"""
    
def sumofdigits(number):
    digitlist = []
    for digit in str(number):
        intdig = int(digit)
        digitlist.append(intdig)
    digitsum = sum(digitlist)
    return digitsum

def factorial(numb):
    factnumblist = range(1,numb+1)
    factnumblist.reverse()
    product=1
    for x in range(len(factnumblist)):
        product=product*factnumblist[x]
    return product

factnum = factorial(100)
output = sumofdigits(factnum)
print output
