#Project Euler Question 17
#Rachel Nash
#Number Letter Counts
#Answer: 21124
"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage."""

totalsum = 0
onedigit = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
teens = {11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
tens = {10:3,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}

def count_letters(num):
    lettersum = 0
    if num in onedigit:
        lettersum+=onedigit[num]
    elif num in teens:
        lettersum+=teens[num]
    elif num in tens:
        lettersum+=tens[num]
    elif num==1000:
        lettersum=11
    else:
        number = str(num)
        if int(number[-2:]) in teens:
            lettersum+= teens[int(number[-2:])]
        else:
            if number[-1]!='0':
                lettersum+= onedigit[int(number[-1])]
            if number[-2]!='0':
                lettersum+= tens[int(number[-2]+'0')]
        if len(number)>2:
            lettersum+=onedigit[int(number[-3])]
            if number[-2:]!='00':
                lettersum+=3 
            lettersum+=7
            
    return lettersum

for x in range(1,1001):
    totalsum+= count_letters(x)
    
print totalsum
