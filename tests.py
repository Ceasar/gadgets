import unittest

import abstract

class testQueue(unittest.TestCase):
  def setUp(self):
    self.queue = abstract.queue()

  def testPushPop(self):
    self.queue.push(0)
    self.assertEqual(self.queue.pop(), 0)

    self.queue.push(0)
    self.queue.push(1)
    self.assertEqual(self.queue.pop(), 0)
    self.assertEqual(self.queue.pop(), 1)

  def testLen(self):
    self.assertEqual(len(self.queue), 0)

    self.queue.push(0)
    self.queue.push(1)
    self.assertEqual(len(self.queue), 2)
    self.queue.pop()
    self.queue.pop()
    self.assertEqual(len(self.queue), 0)

  def testIter(self):
    self.queue.push(0)
    self.queue.push(1)
    for item in self.queue:
    	pass
    self.assertEqual(len(self.queue), 0)

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
