'''A module for converting html tables into csvs.'''

import urllib
import sys

from lxml import etree

def url2csv(url, csv_output, xpath=None):
    '''Convert a webpage into a csv.'''
    tables2csv(csv_output, *find_tables(scrape(url), xpath))

def scrape(url):
    '''Scrapes the content of a webpage.'''
    return urllib.urlopen(url).read()

def find_tables(html, xpath=None):
    '''Finds a table in an html document.'''
    if xpath is None:
        xpath = '//table'
    return etree.HTML(html).xpath(xpath)

def tables2csv(csv_output, *tables):
    '''Turn an html table into an csv.'''
    for index, table in enumerate(tables):
        if index > 0:
            split = csv_output.split('.')
            f = open(split[0] + str(index) + '.' + split[1], 'w')
        else:
            f = open(csv_output, 'w')
        try:
            map(lambda row: f.write(parse_row(row) + '\n'), table.getchildren())
        except:
            f.flush()
        finally:
            f.close()

def parse_row(row):
    '''Parses the content of a row.'''
    return ', '.join([parse_cell(cell) for cell in row.getchildren()])

def parse_cell(cell):
    '''Parse the content of a cell.'''
    return ''.join(cell.itertext()).strip()

if __name__ == '__main__':
  if len(sys.argv) >= 3:
    url2csv(*sys.argv[1:])
