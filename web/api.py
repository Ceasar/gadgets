import urllib
import urllib2
import json


def api(url, token=None):
  """Create an accessor function for an api.

  The accessor takes the path and any GET items and returns the contents
  of the page."""
  def accessor(*args, **kwargs):
    if token is not None:
      kwargs["token"] = token
    path = "".join((url, "/".join([str(arg) for arg in args]), "?", urllib.urlencode(kwargs)))
    page = urllib2.build_opener().open(path)
    return json.loads(page.read())
  return accessor


def scrape(url):
  '''Scrape the content of a webpage.'''
  return urllib.urlopen(url).read()


if __name__ == '__main__':
  import sys
  print scrape(sys.argv[1])
