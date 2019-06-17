from Tree import Tree

tree = Tree(10)

points = [(1,1), (2,2), (4,4), (9,9), (8,8), (8,9), (9,8)]

### INSERTION ###

for p in points:
    tree.insert(p[0], p[1])
    print('\n\nAfter inserting (%d,%d)\n\n' % (p[0], p[1]))
    tree.print_points()

print('\n\n\n\n')


### DELETION ###

# points.reverse()

# for p in points:
#     tree.delete(p[0], p[1])
#     print('\n\nAfter deleting (%d,%d)\n\n' % (p[0], p[1]))
#     tree.print_points()