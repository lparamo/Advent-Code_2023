'''on each row, replace the list of spring conditions with 
five copies of itself (separated by ?) and replace the list of
contiguous groups of damaged springs with five copies of itself
 (separated by ,)
 
So, this row: .# 1
Would become: .#?.#?.#?.#?.# 1,1,1,1,1 '''

##### Leer sobre functools.cache #####

import re
from functools import cache

@cache
def solve():
   return

with open('exampleDay12.txt') as file:
   field=file.read().splitlines()

total=0 #sum of the counts of the different arrangements
for row in field:
   record,groups=row.split(' ')
   record='?'.join([record,record,record,record,record])
   groups=','.join([groups,groups,groups,groups,groups])
   
print(total)