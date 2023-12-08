#It looks like some of the digits are actually spelled out with letters:
#one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
#Equipped with this new information,
#you now need to find the real first and last digit on each line

def part1(line):
    for x in line:
        if x.isdigit():
            a=int(x)
            break
    for x in line:    
        if x.isdigit():
            b=int(x)
    return a*10+b

import re
with open('inputDay1.txt') as file:
    input=file.read().splitlines()
    
digits={'one':'o1e','two':'t2o','three':'t3e','four':'4','five':'5e','six':'6','seven':'7n','eight':'e8t','nine':'9e'}
cont=0
for line in input:
    for x in digits:
        if x in line:
            line=line.replace(x, digits[x])
    cont+=part1(line)  
print(cont)

