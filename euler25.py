#Project Euler Question 25
#Rachel Nash
#1000 Digit Fibonacci Number
#Answer: 4782

"""The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?""" 
def num_digits(num):
    return len(str(num))

fib1 = 1
fib2 = 1
index = 2

while num_digits(fib2) < 1000:
    tmp = fib2
    fib2 = fib1 + fib2
    fib1 = tmp
    index = index +1
    
print index