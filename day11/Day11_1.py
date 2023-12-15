'''The image includes empty space(.) and galaxies(#).
The researcher is trying to figure out the sum of
the lengths of the shortest path between every pair of galaxies.

However, there's a catch: the universe expanded in the time 
it took the light from those galaxies to reach the observatory.

But only rows or columns that contain no galaxies should all 
actually be twice as big.'''
#Expand the universe, then find the length of the shortest path 
#between every pair of galaxies. What is the sum of these lengths?
import math

def cosmic_exp(image):
    rows_no_gal =[]
    for x,row in enumerate(image):
        if all(point == '.' for point in row):
            rows_no_gal.append(x)

    cols_no_gal=[]
    for y, cols in enumerate(zip(*image)): #Iterate over the transpose of image
        if all(point == '.' for point in cols):
            cols_no_gal.append(y)

    w = len(image[0])
    for row in reversed(rows_no_gal):
        image.insert(row, '.' * w)

    h = len(image)
    for col in reversed(cols_no_gal):
        for row in range(h):
            image[row] = image[row][:col] + '.' + image[row][col:]
    return image

def dist(galaxy1,galaxy2): #Taxicab/Manhattan Distance: ∣x1−x2∣+∣y1−y2∣
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

with open('inputDay11.txt') as file:
   universe=file.read().splitlines()

universe=cosmic_exp(universe) #Expand the universe

galaxies=[]
for x,row in enumerate(universe):
    for y, point in enumerate(row):
        if point=='#':
            galaxies.append((x,y))

sum_lengths=0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        sum_lengths+=dist(galaxies[i],galaxies[j])

print(sum_lengths)