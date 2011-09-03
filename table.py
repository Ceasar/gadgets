'''A SQL table representation.'''
import csv

from swap import swap


class Table(object):
    '''A CSV backed SQL table.'''
    @property
    def fieldnames(self):
        with open(self.filename) as f:
            return csv.DictReader(f).fieldnames

    @property.setter
    def fieldnames(self, fieldnames):
        with open(self.filename, 'w') as f:
            dr = csv.reader(f)
            dw = csv.DictWriter(f, fieldnames=fieldnames)
            dw.writerow(dict((field, field) for field in fieldnames))
            for row in self:
                dw.writerow(row)
    
    def __init__(self, filename, fieldnames=None):
        self.filename = filename
        if not fieldnames is None:
            self.fieldnames = fieldnames

    def select(self, columns=None, where=None, as_dict=False):
        '''Select all values from given columns.

        Leave columns as None in order to select all columns.
        Leave where as None in order to select all rows.

        where should take a dictionary representing the row argument as its
        sole parameter and return a boolean.'''
        columns = self.fieldnames if columns is None else columns
        where = (lambda row: True) if where is None else where
        for row in self.named_iter():
            if where(row):
                #this is suboptimal, but a bit more readable
                if as_dict:
                    yield [{column: row[column]} for column in columns]
                else:
                    yield [row[column] for column in columns]

    def update(self, func, as_dict=False):
        '''Apply func to each row.

        Note: if a row should be deleted, return None rather than an empty
        list to delete the row.'''
        #Unfortunately, one cannot just change a line.
        #Instead, one must completely rewrite the file with each change.
        with swap(self.filename) as swp:
            with open(self.filename) as f:
                if as_dict:
                    reader = csv.DictReader(f)
                    writer = csv.DictWriter(swp)
                    fieldnames = reader.fieldnames
                else:
                    reader = csv.reader(f)
                    writer = csv.writer(swp)
                    try:
                        fieldnames = reader.next()
                    except:
                        fieldnames = ''
                writer.writerow(fieldnames)
                for row in reader:
                    updated = func(row)
                    if updated: writer.writerow(updated)

    def append(self, row):
        '''Append a row to the end of the file.'''
        with open(self.filename, 'a') as f:
            if isinstance(row, dict):
                writer = csv.DictWriter(f)
            else:
                writer = csv.writer(f)
            writer.writerow(row)

    def extend(self, rows):
        '''Append mutliple rows to the end of the file.'''
        with open(self.filename, 'a') as f:
            dwriter = csv.DictWriter(f)
            writer = csv.writer(f)
            for row in rows:
                if isinstance(row, dict):
                    dwriter.writerow(row)
                else:
                    writer.writerow(row)

    def __iter__(self):
        #In order to be consistent with named_iter, the header is removed.
        with open(self.filename) as f:
            reader = csv.reader(f)
            header = reader.next()
            for row in reader:
                yield row

    def named_iter(self):
        '''Iterate through the labeled rows.'''
        with open(self.filename, 'rb') as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row

    def __str__(self):
        return self.filename
