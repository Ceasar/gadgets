import copy
import math
import matrix

class Fitter(object):
    '''A handy ui object for fitting data.'''
    def __init__(self):
        self.tuplelist = []

    def add(self, *args):
        '''Add a tuple.'''
        self.tuplelist.append(args)
        for tuplex in self.tuplelist:
            print tuplex

    def fit(self):
        '''Fits a n-degree line through the data.'''
        print project(self.tuplelist)
    

def project(tuplelist):
    '''Takes a list of tuples and fits a curve through them.'''
    #n refers to the degree of the polynomial
    dim = len(tuplelist)

    #Format data.
    xrows = []
    brows = []
    for mytuple in tuplelist:
        xrow = mytuple[:len(mytuple)-1]
        xrow += (1,)
        xrows.append(xrow)
        brows.append([mytuple[len(mytuple)-1]])
    x_matrix = matrix.Matrix(xrows)
    b_matrix = matrix.Matrix(brows)
    x_transpose = x_matrix.transpose()
    
    #Compute inverse of X_transpose * X.
    x_matrix_2 = matrix.multiply(x_transpose, x_matrix)
    x_inv = x_matrix_2.inverse()

    #Computer X_transpose  * b.
    xt_b = matrix.multiply(x_transpose, b_matrix)

    return matrix.multiply(x_inv, xt_b)

def best_fit(A, b):
    '''Takes two matrices and fits a curve through them.'''

    #Format data.
    A_transpose = A.transpose()
    
    #Compute inverse of A_transpose * A.
    At_A = matrix.multiply(A_transpose, A)
    At_A_inv = At_A.inverse()

    #Computer A_transpose * b.
    At_b = matrix.multiply(A_transpose, b)

    return matrix.multiply(At_A_inv, At_b)

def fit_curve(tuplelist):
    '''Takes a list of tuples and fits a curve through them.'''
    dim = len(tuplelist)

    #Format x data.
    xrows = []
    yrows = []
    for mytuple in tuplelist:
        xrow = []
        for n in range(dim):
            xrow.append(math.pow(mytuple[0], n))
        xrows.append(xrow)
        yrows.append([mytuple[1]])
    x_matrix = matrix.Matrix(xrows)
    y_matrix = matrix.Matrix(yrows)

    x_inv = x_matrix.inverse()
    transformation = matrix.multiply(x_inv, y_matrix)
    return transformation
