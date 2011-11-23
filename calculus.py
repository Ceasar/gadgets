from __future__ import division

import math


def differentiate(f, h=1e-3):
  '''Differentiate a function.'''
  def df(x):
    deriv = (f(x + h) - f(x)) / h
    return round(deriv, 3)
  return df


def integrate(f, h=1e-3):
  '''Integrate a function.'''
  def intf(b, a=None):
    if a is None:
      a = 0
    else:
      a, b = b, a
    area = 0
    current = f(a)
    while a <= b: 
      future = f(a+h)
      area += current + future
      current = future
      a += h
    return area * h / 2
  return intf


def find_roots(a, b, c):
  '''Find the roots of a quadratic equation.'''
  root1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
  root2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
  return (root1, root2)
