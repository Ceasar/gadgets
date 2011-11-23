import math

from numpy import array, corrcoef
import numpy.linalg as linalg

class LinearRegression(list):
  '''A linear regression object.'''

  @property
  def slope(self):
    x, y = zip(*self.transformed)
    #Append 1 to the independent variable to get the intercept
    x = zip(x, [1] * len(self))
    coefficients = linalg.lstsq(x, y)[0]
    return coefficients[0]

  @property
  def intercept(self):
    x, y = zip(*self.transformed)
    #Append 1 to the independent variable to get the intercept
    x = zip(x, [1] * len(self))
    coefficients = linalg.lstsq(x, y)[0]
    return coefficients[-1]

  @property
  def correlation(self):
    x, y = zip(*self.transformed)
    return corrcoef(x, y)[0][1]

  @property
  def determination(self):
    return self.correlation ** 2

  @property
  def residuals(self):
    return [y - self.predict(x) for x, y in self.transformed]

  @property
  def transformed(self):
    return map(self._forward, self)

  def _forward(self, point):
    '''Transform a point.'''
    return point

  def _back(self, point):
    '''Transform a point back.'''
    return point

  def predict(self, x):
    '''Get the predicted value of y at x.'''
    return self._back(self.slope * x + self.intercept)

class ExponentialRegression(LinearRegression):
  '''An exponential regression object.'''

  def _forward(self, point):
    '''Transform a point.'''
    x, y = point
    return x, math.log(y)
      
  def _back(self, point):
    '''Transform a point back.'''
    x, y = point
    return x, math.e ** y

class LogisticRegression(LinearRegression):
  '''A logistic regression object.'''
  def __init__(self, points):
    x_vals, y_vals = zip(*points)
    if not all([0 < y < 1 for y in y_vals]):
        raise ValueError("y values should be between 0 and 1.")
    super(LogisticRegression, self).__init__(points)

  def _forward(self, point):
    '''Transform a point.'''
    x, y = point
    return x,  math.log(y / (1.0 - y))
  
  def _back(self, point):
    '''Transform a point back.'''
    x, y = point
    odds = math.e ** y
    return x, odds / (1.0 + odds)


class MultipleRegression(object):
    '''A multiple regression object.'''
    def __init__(self, independents, dependents):
        self.independents = independents
        self.dependents = dependents
    
    @property
    def coefficients(self):
        '''Build a regression line.'''
        #vals = [x + (1,) for x in self.independents]
        return linalg.lstsq(self.independents, self.dependents)[0]

    @property
    def residuals(self):
      return [dep - self.predict(*ind) for ind, dep in zip(self.independents, self.dependents)]

    @property
    def predicted(self):
      return [self.predict(*ind) for ind in self.independents]

    def predict(self, *args):
        '''Get the predicted value of y at x.'''
        #args = [[arg] for arg in args]
        coeffs = array([x for c in self.coefficients for x in c])
        return coeffs.dot(list(args))

class PolynomialRegression(MultipleRegression):
    '''An polynomial regression object.'''
    def __init__(self, points, n):
        super(PolynomialRegression, self).__init__(*zip(*points))
        self.n = n

    @property
    def coefficients(self):
        '''Build a regression line.'''
        transformed = map(self._forward, self.independents)
        independents = self.independents
        self.independents = transformed
        coefficients = super(PolynomialRegression, self).coefficients
        self.independents = independents
        return coefficients

    def _forward(self, x):
        '''Transform a point.'''
        return tuple([x ** n for n in reversed(range(self.n + 1))])

    def predict(self, x):
        '''Get the predicted value of y at x.'''
        return super(PolynomialRegression, self).predict(*self._forward(x))
