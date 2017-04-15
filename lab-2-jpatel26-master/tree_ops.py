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
    return 1 + size(NumTree.left) + size(NumTree.right)

# * 2:
# NumTree -> number
# Returns the number of leaves on the tree
def num_leaves(NumTree):
    leaves = 0
    if NumTree == 'mt':
        return 0
    if NumTree.right == 'mt' and NumTree.left == 'mt':
        return 1
    a = 0
    b = 0
    if NumTree.right!= 'mt':
        a = num_leaves(NumTree.right)
    if NumTree.left != 'mt' :
        b = num_leaves(NumTree.left)
    return a + b


# * 3:
# NumTree -> number
# Returns the sum of the numbers in the tree
def sum(NumTree):
    if NumTree == 'mt':
        return 0
    return NumTree.value + sum(NumTree.right) + sum(NumTree.left)


# * 4:
# NumTree -> number
# Returns the length from the root to the leaves
def height(NumTree):
    if NumTree == 'mt':
        return 0
    if NumTree.right != 'mt':
        a =1 + height(NumTree.right)
    if NumTree.left != 'mt':
        b = 1 + height(NumTree.left)
    if a >= b:
        return a
    if b >= a:
        return b

# * 5:
# NumTree -> Boolean
# Returns true when a node has a leave that is triple the node
def has_triple(NumTree):
    if NumTree == 'mt':
        return 'false'
    if NumTree.right != 'mt' and NumTree.value == 3 * NumTree.right.value:
        return 'true'
    if NumTree.left != 'mt' and NumTree.value == 3 * NumTree.left.value:
        return 'true'
    return has_triple(NumTree.left) or has_triple(NumTree.right)

# * 6:
# NumTree -> NumTree
# Returns a new tree with each element smaller by 1
def sub_one_map(NumTree):
    if NumTree == 'mt':
        return 'mt'
    return TreeNode(NumTree.value - 1, sub_one_map(NumTree.right), sub_one_map(NumTree.left))


# * Tests : the test case class for the tree functions

class TestAll (unittest.TestCase):

    def test_size(self):
        self.assertEqual(size(TreeNode(3, TreeNode(4, 'mt',  'mt'), TreeNode(5,'mt','mt'))),3)
        self.assertEqual(size(TreeNode(3,TreeNode(4, TreeNode(8, 'mt','mt'), TreeNode(12,'mt','mt'), TreeNode(5, 'mt', 'mt')))),5)

    def test_num_leaves(self):
        self.assertEqual(num_leaves(TreeNode(3, TreeNode(4,'mt', 'mt'),TreeNode(5,'mt','mt'))), 2)

    def test_sum(self):
        self.assertEqual(sum(TreeNode(3, TreeNode(4,'mt','mt'), TreeNode(5,'mt','mt'))),12)

    def test_height(self):
        self.assertEqual(height(TreeNode(3, TreeNode(4, TreeNode(6,'mt','mt'), 'mt'), TreeNode(5, 'mt', 'mt'))), 2)

    def test_has_triple(self):
        self.assertEqual(has_triple(TreeNode(3, TreeNode(2, TreeNode(6, 'mt', 'mt'), 'mt'), TreeNode(5, 'mt', 'mt'))), 'true')

    def test_sub_one_map(self):
        self.assertEqual(sub_one_map(TreeNode(3, TreeNode(4, 'mt', 'mt'), TreeNode(5, 'mt', 'mt'))),TreeNode(2, TreeNode(3, 'mt', 'mt'), TreeNode(4, 'mt', 'mt')))

    if (__name__ == '__main__'):
        unittest.main()