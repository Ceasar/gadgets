'''Contains useful functions for analyzing distrubtions of data.'''
from __future__ import division

import math
from math import factorial, sqrt

from counting import combination
from calculus import integrate


def stirling(n):
  '''Get Stirling's approximation to n factorial.'''
  return (n / math.e) ** n  * sqrt(2 * math.pi * n)

class Distribution(object):
  @property
  def mean(self):
    raise NotImplementedError

  @property
  def variance(self):
    raise NotImplementedError

  @property
  def stdev(self):
    return self.variance ** 0.5


class Discrete(object):
  def pmf(self, x):
    raise NotImplementedError

  def cdf(self, b, a=None):
    '''Get the chance that an event occurs between a and b.'''
    if a is None:
      a = 0
    else:
      a, b = b, a
    return sum([self.pmf(k) for k in range(a, b + 1)])


class Continuous(object):
  def pdf(self, b, a=0):
    raise NotImplementedError

  @property
  def cdf(self):
    return integrate(self.pdf)


class Poisson(Distribution, Discrete):
  '''A representation of a Poisson distribution.'''
  #lambda = n * p
  def __init__(self, lambda_):
    self.lambda_ = lambda_

  @property
  def mean(self):
    return self.lambda_

  @property
  def variance(self):
    return self.lambda_

  def pmf(self, k):
    '''Get the value of the pmf at k.'''
    return (self.lambda_ ** k) / factorial(k) * math.e ** -self.lambda_


class Binomial(Distribution, Discrete):
  '''A representation of a binomial distribution.
  
  A binomial distribution is a series of Bernoulli trials.'''
  def __init__(self, n, p):
    self.n = n
    self.p = p

  @property
  def q(self):
    return 1.0 - self.p

  @property
  def mean(self):
    return self.n * self.p

  @property
  def variance(self):
    return self.n * self.p * self.q

  def pmf(self, x):
    '''Get the chance that i success occurs given n trials..'''
    return combination(self.n, x) * (self.p ** x) * (self.q ** (self.n - x))


class Normal(Distribution, Continuous):
  '''A representation of a Normal distribution.'''
  def __init__(self, mu, sigma):
    self.mu = mu
    self.sigma = sigma

  @property
  def mean(self):
    return self.mu

  @property
  def variance(self):
    return self.sigma ** 2

  def pdf(self, x):
    '''Get the density at x.'''
    return 1 / sqrt(2 * math.pi * self.variance) * math.e ** -(((x - self.mu) ** 2) /  (2 * self.variance))


