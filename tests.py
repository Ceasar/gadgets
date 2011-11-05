import unittest

import abstract

class testStack(unittest.TestCase):
  def setUp(self):
    self.stack = abstract.stack()

  def testPushPop(self):
    self.stack.push(0)
    self.assertEqual(self.stack.pop(), 0)

    self.stack.push(0)
    self.stack.push(1)
    self.assertEqual(self.stack.pop(), 1)
    self.assertEqual(self.stack.pop(), 0)

  def testLen(self):
    self.assertEqual(len(self.stack), 0)

    self.stack.push(0)
    self.stack.push(1)
    self.assertEqual(len(self.stack), 2)
    self.stack.pop()
    self.stack.pop()
    self.assertEqual(len(self.stack), 0)

  def testIter(self):
    self.stack.push(0)
    self.stack.push(1)
    for item in self.stack:
    	pass
    self.assertEqual(len(self.stack), 0)


if __name__ == '__main__':
	unittest.main()
