'''on each row, replace the list of spring conditions with 
five copies of itself (separated by ?) and replace the list of
contiguous groups of damaged springs with five copies of itself
 (separated by ,)
 
So, this row: .# 1
Would become: .#?.#?.#?.#?.# 1,1,1,1,1 '''

import re
from itertools import combinations

def is_valid(record, exp_size):
   groups = re.findall(r'#+', record) #find all occurrences of one or more '#'
   real_size = list(map(len, groups)) #returns a list containing the size of the groups.
   return real_size == exp_size

def replace(replacing,sep=','):
   replaced=list()
   for i in range(5):
      replaced.append(replacing)
   return sep.join(replaced)

with open('exampleDay12.txt') as file:
   field=file.read().splitlines()

total=0 #sum of the counts of the different arrangements
for row in field:
   record,groups=row.split(' ')
   record=replace(record,'?')
   groups=replace(groups)
   print(record,'   ',groups)
   group_sizes=list(map(int,groups.split(',')))
   total_sp=sum(group_sizes)
   not_damaged_sp= total_sp - record.count('#') #initially not damaged
   unknown_sp_pos=[] #positions of the unknown springs
   for i, char in enumerate(record):
      if char == '?':
         unknown_sp_pos.append(i)
   
   count=0 #count all of the different arrangements
   for assignment in combinations(unknown_sp_pos, not_damaged_sp):
      posible_record=list(record)
      for pos in assignment:
         posible_record[pos]='#'
      if is_valid(''.join(posible_record),group_sizes):
         count+=1

   total+=count
print(total)