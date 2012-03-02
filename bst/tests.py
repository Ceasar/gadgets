import unittest

from binarytree import BinaryTree, BinarySearchTree

class BinaryTreeTest(unittest.TestCase):
    def test_height_2(self):
        bst = BinaryTree([2, 3, 1])
        self.assertTrue(bst.height == 2)

    def test_height_3(self):
        bst = BinaryTree([2, 3, 1, 4])
        self.assertTrue(bst.height == 3)

    def test_height_3(self):
        bst = BinaryTree([2, 3, 1, 4])
        self.assertTrue(bst.height == 3)

    def test_size(self):
        bst = BinaryTree([2, 3, 1, 4])
        self.assertTrue(bst.size == 4)

    def test_iter(self):
        bst = BinaryTree([2, 3, 1, 4])
        self.assertTrue(list(bst) == [2, 3, 1, 4])

    def test_contains(self):
        bst = BinaryTree([2, 3, 1, 4])
        self.assertTrue(4 in bst)

    def test_not_contains(self):
        bst = BinaryTree([2, 3, 1, 4])
        self.assertTrue(5 not in bst)


class SentinelTest(unittest.TestCase):
    def test_sentinel(self):
        bst = BinaryTree()
        self.assertTrue(bst.sentinel)

    def test_sentinel_empty_list(self):
        bst = BinarySearchTree([])
        self.assertTrue(bst.sentinel)

class BinarySearchTreeTest(unittest.TestCase):
    def test_sorted_init_val(self):
        bst = BinarySearchTree([1, 2, 3])
        self.assertTrue(bst.val == 2)

    def test_sorted_init_left(self):
        bst = BinarySearchTree([1, 2, 3])
        self.assertTrue(bst.left.val == 1)

    def test_sorted_init_right(self):
        bst = BinarySearchTree([1, 2, 3])
        self.assertTrue(bst.right.val == 3)

    def test_unsorted_init_val(self):
        bst = BinarySearchTree([2, 3, 1])
        self.assertTrue(bst.val == 2)

    def test_unsorted_init_left(self):
        bst = BinarySearchTree([2, 3, 1])
        self.assertTrue(bst.left.val == 1)

    def test_unsorted_init_right(self):
        bst = BinarySearchTree([2, 3, 1])
        self.assertTrue(bst.right.val == 3)

    def test_unsorted_init_right(self):
        bst = BinarySearchTree([2, 3, 1])
        self.assertTrue(bst.right.val == 3)




if __name__ == "__main__":
    unittest.main()
