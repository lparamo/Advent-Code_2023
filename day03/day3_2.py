#A gear is any '*' symbol that is adjacent to exactly two part numbers.
#Its gear ratio is the result of multiplying those two numbers together.
#This time, you need to find the gear ratio of every gear and add them all up.
import re
import math

with open('inputDay3.txt') as file:
    schem=list(file)
    
sum_ratio=0
possiblegear=[] #positions of possible gears '*'
for i in range(len(schem)-1):
    for j in range(len(schem[0])-1):
        if schem[i][j]=='*':
            possiblegear.append((i,j))
dic={}
for g in possiblegear:
    dic[g]=[]    
for i, line in enumerate(schem):
    for num in re.finditer(r'\d+', line): #\d matches any digit from 0 to 9 in a target string (line),+ indicates num can contain any number of digits.
        gear=0 #see if num is "gear"
        for n in (i-1,i,i+1):
            for m in range(num.start()-1,num.end()+1):
                if (n,m) in possiblegear:
                    dic[(n,m)].append(int(num.group()))
for i in dic:
    if len(dic[i])==2:
        sum_ratio+=dic[i][0]*dic[i][1]
print(sum_ratio)
