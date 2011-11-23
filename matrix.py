import copy

alist = [[1.0, 4.0, 9.0], [1.0, 3.0, 4.0], [7.0, 3.0, 6.0]]
blist = [[1.0, 2.0], [3.0, 2.0], [3.0, 2.0]]

def multiply(a,b):
    '''Multiply two matrices.'''
    if a.n != b.m:
        raise
    result = []
    for arow in a.rows:
        newrow = []
        for col in range(b.n):
            index = -1
            total = 0
            for brow in b.rows:
                index += 1
                total += arow[index] * brow[col]
            newrow.append(round(total, 5))
        result.append(newrow)
    return Matrix(result)

def identity(n):
    '''Returns an nxn identity matrix.'''
    rows = []
    for r_num in range(n):
        row = []
        for c_num in range(n):
            if r_num == c_num:
                row.append(1)
            else:
                row.append(0)
        rows.append(row)
    return Matrix(rows)

class Matrix():
    '''Create a matrix suitable for linear algebra.'''
    def __init__(self, matrix):
        self.rows = matrix
        self.m = len(self.rows)
        self.n = len(self.rows[0])

    def append_row(self, row):
        '''Append a row to the matrix.'''
        self.rows.append(row)
        self.m += 1

    def augment(self, other):
        '''Augment the matrix.'''
        if self.m != other.m:
            raise
        for index in range(other.m):
             self.rows[index] += other.rows[index]
        self.n += other.n

    def get_vectors(self):
        '''Get a list of the vectors in the matrix.'''
        vectors = []
        for col in range(self.n):
            vector = []
            for row in self.rows:
                element = row[col]
                vector.append(element)
            vectors.append(vector)
        return vectors

    def split(self, index):
        '''Split the matrix into two at the index.'''
        left = []
        right = []
        for row in self.rows:
            left.append(row[0:index])
            right.append(row[index:self.n])
        return (Matrix(left), Matrix(right))

    #---ROW OPERATIONS
    def swap(self, i, j):
        '''Swap row i with row j'''
        temp = self.rows[i]
        self.rows[i] = self.rows[j]
        self.rows[j] = temp

    def scale_row(self, i, scalar):
        '''Scale row i by a scalar.'''
        target_row = self.rows[i]
        for col in range(len(target_row)):
            #print "col: " + str(col)
            target_row[col] *= scalar
        return target_row

    def add_rows(self, i, j):
        '''Add row i to row j.'''
        for col in range(self.n):
            adding_element = self.rows[i][col]
            self.rows[j][col] += adding_element
        return self.rows[j]

    #Functions to get useful forms of the matrix.
    def R(self):
        '''Get the reduced form of the matrix.'''
        result = Matrix(copy.deepcopy(self.rows))
        maxrank = min(result.m, result.n)
        for rank in range(maxrank):
            rows = result.rows
            pivot_row = rows[rank]
            pivot = pivot_row[rank]
            if pivot == 0:
                #Finds a new row to use and swaps this one out.
                for row in rows[rank: result.m]:
                    if row[rank] != 0:
                        result.swap(rows.index(row), rank)
                        break
                pivot_row = rows[rank]
                if pivot_row[rank] == 0:
                    continue
            for row in range(result.m):
                if row == rank:
                    continue
                element_row = rows[row]
                element = element_row[rank]
                if element != 0:
                    pivot = pivot_row[rank]
                    result.scale_row(rank, -float(element)/pivot)
                    result.add_rows(rank, row)
            pivot = pivot_row[rank]
            result.scale_row(rank, 1.0/pivot)
        return result

    def inverse(self):
        '''Get the inverse of the matrix.'''
        result = Matrix(copy.deepcopy(self.rows))
        result.augment(identity(result.n))
        reduced = result.R()
        return reduced.split(self.n)[1]

    def transpose(self):
        '''Get the transpose of the matrix.'''
        result_rows = []
        for index in range(self.n):
            result_rows.append([])
        for row in self.rows:
            for n in range(self.n):
                result_rows[n].append(row[n])
        result = Matrix(result_rows)
        return result

    def U(self):
        '''Get the upper-triangular form of the matrix.'''
        result = Matrix(copy.deepcopy(self.rows))
        maxrank = min(result.m, result.n)
        for rank in range(maxrank):
            rows = result.rows
            pivot_row = rows[rank]
            pivot = pivot_row[rank]
            if pivot == 0:
                #Finds a new row to use and swaps this one out.
                for row in rows[rank: result.m]:
                    if row[rank] != 0:
                        result.swap(rows.index(row), rank)
                        break
                pivot_row = rows[rank]
                if pivot_row[rank] == 0:
                    continue
            for row in range(rank + 1, result.m):
                element_row = rows[row]
                element = element_row[rank]
                if element != 0:
                    pivot = pivot_row[rank]
                    result.scale_row(rank, -float(element)/pivot)
                    result.add_rows(rank, row)
                    result.scale_row(rank, pivot/-float(element))
        return result

    def __str__(self):
        for row in self.rows:
            print row
        return str(self.m) + "x" + str(self.n)

A = Matrix(alist) 
B = Matrix(blist)
