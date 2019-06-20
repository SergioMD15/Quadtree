from Tree import Tree
import random
import time

size = 10

#### FIRST EXPERIMENT ####

tree = Tree(size)

### INSERTION ###

points = [(1,1), (2,2), (4,4), (9,9), (8,8), (8,9), (9,8)]

for p in points:
    tree.insert(p[0], p[1])
    tree.print_points()

print('\n\n\n\n')


### DELETION ###

for p in points:
    tree.delete(p[0], p[1])
    tree.print_points()


#### SECOND EXPERIMENT ####

values = random.sample(range(1000), 500)

points = [(i, t) for i in values for t in values]

size = 1000000

tree = Tree(size)

times = []

for i in range(len(points)):
    start = time.time()
    tree.insert(points[i][0], points[i][1])
    end = time.time()
    times.append((i,end-start))