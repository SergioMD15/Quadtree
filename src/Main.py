from Tree import Tree

tree = Tree(10)

tree.insert(1,1)

print('\n\n After inserting (1,1) \n\n')

tree.print_points()

tree.insert(2,2)

print('\n\n After inserting (2,2) \n\n')

tree.print_points()

tree.insert(4,4)

print('\n\n After inserting (4,4) \n\n')

tree.print_points()

tree.insert(9,9)

print('\n\n After inserting (9,9) \n\n')

tree.print_points()

tree.insert(8,8)

print('\n\n After inserting (8,8) \n\n')

tree.print_points()

tree.insert(8,9)

print('\n\n After inserting (8,9) \n\n')

tree.print_points()

tree.insert(9,8)

print('\n\n After inserting (9,8) \n\n')

tree.print_points()

tree.delete(1,1)

print('\n\n After deleting (1,1) \n\n')

tree.print_points()

tree.delete(4,4)

print('\n\n After deleting (4,4) \n\n')

tree.print_points()