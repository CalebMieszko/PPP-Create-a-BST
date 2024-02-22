# Part 1: Create a BSTNode class

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
      self.data = data
      self.left = left
      self.right = right

    def __str__(self):
       return str(self.data)

    def __repr__(self):
       return str(self.data)


# Part 2: Create a BST class
# Part 3: Add functionality to your BST class

class BST:
    def __init__(self, root=None):
      self.root = root
      self.contents = []

    def __str__(self):
      if self.root == None:
         return "The tree is empty"
      else:
         self.output = ''
         self.print_tree(node=self.root)
         return self.output

    def __repr__(self):
      if self.root == None:
         return "The tree is empty"
      else:
         self.output = ''
         self.print_tree(node=self.root)
         return self.output

    def print_tree(self, node, level=0):
      if node != None:
         self.print_tree(node.right, level + 1)
         self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
         self.print_tree(node.left, level + 1)

    def add(self, node):
       if type(node) != int and type(node) != BSTNode:
          raise ValueError(
              "Please pass in an int or a BSTNode. No other data type will be accepted.")
       if type(node) == int:
          node = BSTNode(node)
       if node.data in self.contents:
          return
       if self.root == None:
          self.root = node
          self.contents.append(node.data)
          return
       self.add_node(self.root, node)

    def add_node(self, current_node, new_node):
        if new_node.data > current_node.data:
           if current_node.right == None:
              current_node.right = new_node
              self.contents.append(new_node.data)
              return
           else:
              self.add_node(current_node.right, new_node)
        else:
           if current_node.left == None:
              current_node.left = new_node
              self.contents.append(new_node.data)
              return
           else:
              self.add_node(current_node.left, new_node)


# If the tree is empty (root points to None), put the new node at the top of the tree.
    # If the tree is not empty, start at the root.
    # Compare the new node's value to the current node's value.
        # If the new node is bigger, move to the right.
        # If the new node's value is smaller, move to the left.
        # When there is no node at the current position, put the new node there.
