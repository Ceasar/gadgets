'''A SQL table representation.'''

from collections import namedtuple


class Table(list):
    '''Make a table with specified columns and rows.'''
    def __init__(self, name='Row', columns=(), rows=[]):
        self.name = name
        self.columns = tuple(columns)
        self.Row = namedtuple(name, columns)
        super(Table, self).__init__([self.Row(*row) for row in rows])
    
    def select(self, columns):
        '''Select all values from given columns.'''
        if hasattr(columns, '__iter__'):
            columns = [columns]
        nrow = namedtuple('Row', columns)
        for row in self:
            yield nrow([getattr(row, column) for column in columns])

    def where(self, condition):
        '''Select all vectors matching the conditions.'''
        for row in self:
            if condition(row):
                yield row

    def write(self, filename):
        '''Writes the table as a csv to a file.'''
        with open(filename, 'w') as f:
            f.write(', '.join(self.columns))
            map(lambda row: f.write(', '.join([str(field) for field in row])), self.rows)
    
    def append(self, item):
        super(Table, self).append(self.Row(item))

    def __setitem__(self, i, y):
        raise NotImplementedError

    def __str__(self):
        return self.name

class CSV(Table):
    '''A representation of a CSV.'''
    def __init__(self, filename, name='Row'):
        with open(filename) as f:
            columns = [col.strip() for col in f.readline().split(',')]
            rows = [line.strip().split(',') for line in f]
            super(CSV, self).__init__(name, columns, rows)
