from Tree import Tree

tree = Tree(4)

tree.insert(1,1)
tree.insert(2,1)

point = tree.find(1,1)
if(point):
    point.print_point()

point = tree.find(2,1)
if(point):
    point.print_point()
