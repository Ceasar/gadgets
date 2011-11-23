'''A collection of methods for analyzing data.'''
from __future__ import division
from collections import defaultdict
import math

class Sample(list):

  @property
  def mean(self):
    '''Get the mean.'''
    return sum(self) / len(self)

  @property
  def median(self):
    '''Get the median.'''
    clone = self[:]
    clone.sort()
    return clone[len(self) / 2]

  @property
  def mode(self):
    '''Get the mode.'''
    frequency = self.frequency
    return max(frequency, key=lambda x: frequency[x])

  @property
  def variance(self):
    '''Calculate the variance.'''
    xbar = self.mean
    return sum([(x - xbar) ** 2 for x in self]) / (len(self) - 1)

  @property
  def stdev(self):
    '''Calculate the standard deviation.'''
    return math.sqrt(self.variance)

  def covariance(self, other):
    '''Calculate the covariance of two selfs.'''
    assert len(self) == len(other), 'Samples are not the same size.'
    n = len(self)
    xbar, ybar = self.mean, other.mean
    return sum([(x - xbar) * (y - ybar) for x, y in zip(self, other)]) / (n - 1)

  def correlation(self, other):
    '''Calculate the correlation between two selfs.'''
    assert len(self) == len(other), 'Samples are not the same size.'
    return self.covariance(other) / (self.stdev * other.stdev)

  @property
  def frequency(self):
    '''Calculate the frequency of each value.'''
    counts = defaultdict(int)
    for val in self:
      counts[val] += 1
    return dict(counts)

  @property
  def relative_frequency(self):
    '''Calculate the relative frequency of each value.'''
    frequency = self.frequency
    n = len(self)
    for key in frequency:
      frequency[key] /= n 
    return frequency

class ProbabilityMassFunction(dict):
  '''A dictionary object, where k, v corresponds to value, probability.'''
  @property
  def expected_value(self):
    '''Get the expected value.''' 
    return sum([self[value] * value for value in self])

  @property
  def expected_variance(self):
    '''Get the expected variance.'''
    expected = self.expected_value
    return sum([self[value] * (expected - value) ** 2 for value in self])
