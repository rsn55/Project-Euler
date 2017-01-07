#Project Euler Question 9
#Rachel Nash
#Special Pythagorean Triplet
#Answer:31875000
"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc."""

for a in range(1,1000):
    for b in range(1,1000):
        c = (a**2+b**2)**0.5
        if (a+b+c==1000):
            break
        b+=1
    if (a+b+c==1000):
        break
    a+=1
print int(a*b*c)
        

        
