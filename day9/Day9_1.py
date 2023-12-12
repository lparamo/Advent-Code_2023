'''Each line in the report contains the history of a single value.

Analyze your report and extrapolate the next value for each history.
What is the sum of these extrapolated values?'''

import re

def next_val(sequence): #recursive function
    if len(sequence) == 0:
         return 0
    new_seq = [sequence[i+1]-sequence[i] for i in range(len(sequence)-1)]
    return sequence[-1]+ next_val(new_seq)

with open('inputDay9.txt') as file:
    input=file.read().splitlines()

sum_values=0
for history in input:
    values = [int(x) for x in history.split()]
    next = next_val(values)
    sum_values+=next

print(sum_values)
        
    
    
