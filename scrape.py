import sys
import urllib


def scrape(url):
  '''Scrapes the content of a webpage.'''
  return urllib.urlopen(url).read()

if __name__ == '__main__':
  print scrape(sys.argv[1])
