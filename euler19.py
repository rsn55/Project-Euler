#Project Euler Question 19
#Rachel Nash
#Counting Sundays
#Answer: 171

"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
weekdays = {1:'no',2:'no',3:'no',4:'no',5:'no',6:'no',7:'Sunday'}

sundayTotal = 0
trackDay = 2 #1 Jan 1901 is a Tuesday
for year in range(1901,2001):
    if (year%4.0==0 and year%100.0!=0) or (year%400.0==0):
        months[2]=29
    for month in range(1,13):
        for day in range(1,months[month]+1):
            if weekdays[trackDay]=='Sunday':
                trackDay = 1
                if day==1:
                    sundayTotal +=1
            else:
                trackDay+=1
    months[2]=28
print sundayTotal


    
    
    
    