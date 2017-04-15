import unittest
# * Section 2 (Trees)

# * dd: NumTree Data Definition
# A NumTree is one of
# -'mt'
# - a TreeNode

class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        #boilerplate omitted
    def __eq__(self,other):
        return type(other) == TreeNode and self.value == other.value and self.left == other.left and self.right == other.right
    def __repr__(self):
        return ("TreeNode(%s, %s, %s)" % (self.value, self.left, self.right))

# * 1:
# NumTree -> number
# Returns the number of elements in the tree
def size(NumTree):
    if NumTree == 'mt':
        return 0
    return 1 + size(TreeNode(NumTree.value, NumTree.right, NumTree.left,))

# * 2:
# NumTree -> number
# Returns the number of leaves on the tree
def num_leaves(NumTree):
    leaves = 0
    if NumTree == 'mt':
        return 0
    if NumTree.right == 'mt' and NumTree.left == 'mt':
        leaves += 1
    if NumTree.right!= 'mt':
        num_leaves(NumTree.right)
    if NumTree.left != 'mt' :
        num_leaves(NumTree.left)


# * 3:
# NumTree -> number
# Returns the sum of the numbers in the tree
def sum(NumTree):
    total = 0
    if NumTree == 'mt':
        return total
    if NumTree.left == 'mt' and NumTree.right == 'mt':
        return total
    return sum(NumTree.right) + sum(NumTree.left)


# * 4:
# NumTree -> number
# Returns the length from the root to the leaves
def height(NumTree):

# * 5:
# NumTree -> Boolean
# Returns true when a node has a leave that is triple the node
def has_triple(NumTree):

# * 6:
# NumTree -> NumTree
# Returns a new tree with each element smaller by 1

# * Tests : the test case class for the tree functions

class TestAll (unittest.TestCase):

    if (__name__ == '__main__'):
        unittest.main()