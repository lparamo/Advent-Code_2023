#There are lots of numbers and symbols you don't really understand,
#but apparently any number adjacent to a symbol, even diagonally,
#is a "part number" and should be included in your sum.
#(Periods '.' do not count as a symbol.)
#What is the sum of all of the part numbers in the engine schematic?
import re
import math

with open('inputDay3.txt') as file:
    schem=list(file)
    
sum_pnums=0
sympos=[] #positions of symbols
for i in range(len(schem)-1):
    for j in range(len(schem[0])-1):
        if schem[i][j] not in '0123456789.':
            sympos.append((i,j))

for i, line in enumerate(schem):
    for num in re.finditer(r'\d+', line): #\d matches any digit from 0 to 9 in a target string (line),+ indicates num can contain any number of digits.
        pnum=0 #see if num is "part number"
        for n in (i-1,i,i+1):
            for m in range(num.start()-1,num.end()+1):
                if (n,m) in sympos:
                    pnum=int(num.group())
        sum_pnums+=pnum    
print(sum_pnums)
