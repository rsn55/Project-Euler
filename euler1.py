# Project Euler Question 1
# Rachel Nash
# Multiples of 3 and 5
# Answer: 233168

"""If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

naturalList = range(1,1000)
listOfMultiples = []
for x in naturalList:
    if (x%3 == 0) or (x%5 == 0):
        listOfMultiples.append(x)
sumOfMultiples = sum(listOfMultiples)
print sumOfMultiples