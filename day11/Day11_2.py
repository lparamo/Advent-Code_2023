'''Now, instead of the expansion you did before, make each 
empty row or column one million times larger.That is, 
each empty row should be replaced with 1000000 empty rows, and 
each empty column should be replaced with 1000000 empty columns.'''
import math

def new_ubication(galaxy, mult):
    rows_no_gal_before = 0 #rows without galaxy before our current galaxy
    for row in rows_no_gal:
        if row < galaxy[0]:
            rows_no_gal_before +=1
    cols_no_gal_before = 0 #cols without galaxy before our current galaxy
    for col in cols_no_gal:
        if col < galaxy[1]:
            cols_no_gal_before+=1
    return (galaxy[0] + rows_no_gal_before * (mult - 1),
            galaxy[1] + cols_no_gal_before * (mult - 1))

def dist(galaxy1,galaxy2): #Taxicab/Manhattan Distance: ∣x1−x2∣+∣y1−y2∣
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

with open('inputDay11.txt') as file:
   universe=file.read().splitlines()

#We don't expand the universe per se, it would be too much to iterate.
#We calculate the new ubication of the galaxies instead.

rows_no_gal =[] #rows without galaxy
for x,row in enumerate(universe):
    if all(point == '.' for point in row):
        rows_no_gal.append(x)

cols_no_gal=[] #cols without galaxy
for y, cols in enumerate(zip(*universe)):
    if all(point == '.' for point in cols):
        cols_no_gal.append(y)

galaxies=[]
for x,row in enumerate(universe):
    for y, point in enumerate(row):
        if point=='#':
            new_x, new_y = new_ubication((x, y), 1000000)
            galaxies.append((new_x, new_y))

sum_lengths=0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        sum_lengths+=dist(galaxies[i],galaxies[j])

print(sum_lengths)