import unittest
# * Section 1 (Lists)

# * dd: NumList Data Definition
# a NumList is one of
# - "empty"
# - a Pair

class Pair:
    def __init__ (self, first, rest):
        self.first = first
        self.rest = rest
    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest
    def __repr__ (self):
        return ("Pair(%s, %s)" % (self.first, self.rest))

# * 1:
# NumList -> number
# returns the number of values in a list
def length(NumList):
    if NumList == 'mt':
        return 0
    return 1 + length(NumList.rest)

# * 2:
# NumList - number
# returns the sum of the values in the list
def sum(numlist):
    if (numlist == "mt"):
        return 0
    else:
        return numlist.first + sum(numlist.rest)


# * 3:
# Numlist number(Threshold) -> number
# Returns number of values that are greater than threshold
def count_greater_than(numlist, threshold):
    if numlist == 'mt':
        return 0
    if numlist.first > threshold:
        return 1 + count_greater_than(numlist.rest, threshold)
    if numlist.first <= threshold:
        return count_greater_than(numlist.rest, threshold)

# * 4:
# Numlist number(value) -> number
# Returns the position of value in the numlist
# i is an accumulator starting at 0
def find (NumList, value, i = 0):
    if NumList == 'mt':
        return None
    if NumList.first == value:
        return i
    return find (NumList.rest, value, i +1 )


# * 5:
# NumList -> Numlist
# Returns a new list with each term smaller by 1
def sub_one_map(NumList):
    if NumList == 'mt':
        return 'mt'
    return Pair(NumList.first - 1, sub_one_map(NumList.rest))

# * 6:
# NumList number-> Numlist
# Returns a new list with additional term added
def insert(NumList, newnum):
    if NumList == 'mt':
        return Pair( newnum, 'mt')
    if newnum >= NumList.first:
        return Pair(NumList.first, insert (NumList.rest, newnum))
    if newnum < NumList.first:
        return Pair(newnum, copy(NumList))

#numlist-> numlist
# Coppies numlist into another list
def copy(numlist):
    if numlist == 'mt':
        return 'mt'
    return Pair(numlist.first, copy(numlist.rest))



# * Tests : the test case class for the list functions

class TestAll (unittest.TestCase):

    def test_length(self):
        self.assertEqual(length(Pair(3,Pair(2,Pair(4,'mt')))),3)

    def test_sum(self):
        self.assertEqual(sum(Pair(3, Pair(2, Pair(4, 'mt')))), 9)

    def test_count_greater_than(self):
        self.assertEqual(count_greater_than(Pair(3,Pair(2,Pair(4,'mt'))),2),2)
    def test_find(self):
        self.assertEqual(find((Pair(3,Pair(2,Pair(4,'mt')))), 2),1)

    def test_sub_one_map(self):
        self.assertEqual(sub_one_map((Pair(3, Pair(2, Pair(4, 'mt'))))),(Pair(2, Pair(1, Pair(3, 'mt')))))

    def test_insert(self):
        self.assertEqual(insert(Pair(1, Pair(8, Pair(23, 'mt'))),13),Pair(1,Pair(8,Pair(13,Pair(23,'mt')))))

if (__name__ == '__main__'):
    unittest.main()

