#Project Euler Question 4
#Rachel Nash
#Largest Palindrome Product
#Answer: 906609
"""A palindromic number reads the same both ways. The largest palindrome made from the product of 2 two-digit number is 9009.
This comes from multiplying 91 and 99.
Find the largest palindrome made from the product of two 3-digit numbers."""
def ispalindrome(x):
    list=[]
    for y in str(x):
        list.append(y)
    reversed=list[:]
    reversed.reverse()
    if len(list)==1:
        return True
    if list==reversed:
        return True
    else:
        return False
 
pal = 10201
testing = range(101,1000)
testing.reverse()
for x in testing:
    for i in testing:
        possible = x*i
        if ispalindrome(possible) and possible>pal:
            pal=possible
    
print pal
