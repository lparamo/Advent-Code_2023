'''In the giant field just outside, the springs are arranged into rows.
For each row, the condition records show every spring and whether 
it is operational (.) or damaged (#).
This is the part of the condition records that is itself damaged;
 for some springs, it is simply unknown (?)
  
However, the engineer that produced the condition records also
duplicated some of this information in a different format! 
After the list of springs for a given row, the size of each 
contiguous group of damaged springs is listed in the order
those groups appear in the row. '''

#For each row, count all of the different arrangements of 
#operational and broken springs that meet the given criteria.
#What is the sum of those counts?
import re
from itertools import combinations

def is_valid(record, exp_size):
   groups = re.findall(r'#+', record) #find all occurrences of one or more '#'
   real_size = list(map(len, groups)) #returns a list containing the size of the groups.
   return real_size == exp_size


with open('inputDay12.txt') as file:
   field=file.read().splitlines()

total=0 #sum of the counts of the different arrangements
for row in field:
   record,groups=row.split(' ')
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