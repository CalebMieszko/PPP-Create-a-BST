"""
Part 1: Create a BSTNode class


** Creating a BST Node Class **

This class will look very similar to the Node class we wrote for our linked list, but should fulfill the following requirements:

The constructor should accept up to three arguments: data, left, and right
   If any of the arguments are not specified, they should default to data=None.
   Don't forget to include the self argument.

   Write two magic methods (__str__() and __repr__() ) to allow the nodes to be printed. 
      These two magic methods should return strings that represent the node. 
      They should both return the value of the node's data as a "string".

         To test that these work, a node with the value 3 for its data should output 3 when printed.
         Use the code at the end to test whether your BSTNode is functioning correctly.

"""


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


"""
Part 2: Create a BST class
"""


class BST:
    def __init__(self, root=None):
        self.root = root
        self.contents = []

    def __str__(self):
        if self.root == None:
            return "The tree has no root."
        else:
            self.output = ''
            self.print_tree(node=self.root)
            return self.output

    def __repr__(self):
        if self.root == None:
            return "The tree has no root."
        else:
            self.output = ''
            self.print_tree(node=self.root)
            return self.output

    def print_tree(self, node, level=0):
        if node != None:
            self.print_tree(node.right, level + 1)
            self.output += ' ' * 4 * level + '-> ' + str(node.data) + ' '
            self.print_tree(node.left, level + 1)

    def add(self, node):
        # raise an error if the wrong data type is submitted
        if type(node) != int and type(node) != BSTNode:
            raise ValueError(
                "You did not enter an int or a BSTNode. Please enter the correct data and try again.")

        # if data is an int, build a node
        if type(node) == int:
            node = BSTNode(node)

        # if we already have the node
        if node.data in self.contents:
            return

        # if the tree is empty
        if self.root == None:
            self.root = node
            self.contents.append(node.data)
            return

        self.add_node(self.root, node)

    def add_node(self, current_node, new_node):
        if new_node.data > current_node.data:
            if current_node.right == None:
                current_node.right == new_node
                self.contents.append(new_node)
                return
            else:
                self.add_node(current_node.right, new_node)
        else:
            if current_node.left == None:
                current_node.left == new_node
                self.contents.append(new_node)
                return
            else:
                self.add_node(current_node.left, new_node)


"""
** Test your code **

node1 = BSTNode(3)
print(node1)  # 3

node2 = BSTNode(4, left=node1)
print(node2)  # 4

node3 = BSTNode()
print(node3)  # None
node3.data = 5
print(node3)  # 5


# create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)


bst = BST()
print(bst)

bst.root = node2
print(bst)

node2.right = node3
print(bst)
"""
