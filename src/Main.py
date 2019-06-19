from Tree import Tree

size = 100

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

tree.print_points_reversed()