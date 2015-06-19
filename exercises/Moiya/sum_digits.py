#! /usr/bin/env python
import sys
print sys.argv

def sum_digits(x):
    sum = 0
    while x>0:
        num = x%10
        sum+=num
        x = x/10
    return sum

number = input ('Count by: ')
end = raw_input ('Stop at: ') or 'None'

if end == 'None':
    for i in range(1,number+1):
        x = number*i
        tot = sum_digits(x)
        print tot
else:
    for i in range(1, int(end)/number+1):
        x = number*i
        tot = sum_digits(x)
        print tot
