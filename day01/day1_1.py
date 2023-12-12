#On each line, the calibration value can be found by combining
#the first digit and the last digit (in that order) to form a single two-digit number
#Consider your entire calibration document.
#What is the sum of all of the calibration values?

import re
with open('inputDay1.txt') as file:
    input=file.read().splitlines()
    
    sum_val=0
    for line in input:
        for x in line:
            if x.isdigit():
                a=int(x) #first digit
                break
        for x in line:    
            if x.isdigit():
                b=int(x) #last digit
            
        sum_val+=a*10+b
        
print(sum_val)
