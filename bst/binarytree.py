

class BinaryTree(object):
    def __init__(self, items=None):
        if items:
            items = list(items)
            m = len(items) / 2
            left, mid, right = items[:m], items[m], items[m + 1:]
            self.left = BinaryTree(left)
            self.val = mid
            self.right = BinaryTree(right)
        else:
            self.left, self.val, self.right = None, None, None

    @property
    def sentinel(self):
        return self.val is None

    @property
    def height(self):
        return 0 if self.sentinel else 1 + max(self.left.height, self.right.height)

    def __iter__(self):
        """Iterate over the items in order."""
        if self.sentinel:
            pass
        else:
            for e in self.left:
                yield e
            yield self.val
            for e in self.right:
                yield e
    @property
    def size(self):
        return sum(1 for _ in self)

    def __str__(self):
        if self.sentinel:
            return "Empty"
        else:
            return "Node (%s) %s (%s)" % (self.left, self.val, self.right)

    def __repr__(self):
        if self.sentinel:
            return "Empty"
        else:
            return "Node (%s) %s (%s)" % (self.left, self.val, self.right)


class BinarySearchTree(BinaryTree):
    def __init__(self, items=None):
        items = list(sorted(items))
        if items:
            m = len(items) / 2
            left, mid, right = items[:m], items[m], items[m + 1:]
            self.left = BinarySearchTree(left) if left else None
            self.val = mid
            self.right = BinarySearchTree(right) if right else None
        else:
            self.left, self.val, self.right = None, None, None

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = BinarySearchTree([val])
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BinarySearchTree([val])
            else:
                self.right.insert(val)
