linea='Game 1: 3 blue, 4 red; 18 red, 2 green, 6 blue; 2 green'
import re
list=re.split(': |, |; | ',linea)
print(list)
def ispossible(lista):
    for i in range(3,len(list),2):
        if list[i]=='red':
            if int(list[i-1])>12:
                return False
        elif list[i]=='green':
            if int(list[i-1])>13:
                return False
        else:
            if int(list[i-1])>14:
                return False
    return True

print(ispossible(list))
    
