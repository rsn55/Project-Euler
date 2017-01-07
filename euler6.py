#Project Euler Question 6
#Rachel Nash
#Sum Square Difference
# Answer: 25164150

"""The sum of the squares of the first ten natural numbers is
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is
    (1 + 2 + ... + 10)^2 = 552 = 3025
    Hence the difference between the sum of the squares
    of the first ten natural numbers and the square of
    the sum is 3025 - 385 = 2640.
    Find the difference between the sum of the squares
    of the first one hundred natural numbers and the square of the sum."""
    
n=100
sumOfSquares = (n*(n+1)*(2*n+1))/6
sumNum = sum(range(1,n+1))
squareOfSum = sumNum**2
diff = squareOfSum - sumOfSquares
print diff