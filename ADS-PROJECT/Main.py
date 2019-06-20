from Tree import Tree
import random
import time

size = 100

#### FIRST EXPERIMENT ####

tree = Tree(size)

### INSERTION ###

for p in range(size):
    for p2 in range(size):
        tree.insert(p, p2)
        tree.print_points()

print('\n\n\n\n')


### DELETION ###

for p in range(size - 1, -1, -1):
    for p2 in range(size - 1, -1, -1):
        tree.print_points()
        tree.delete(p, p2)

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