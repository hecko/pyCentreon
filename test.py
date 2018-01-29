#!/usr/bin/env python

from pprint import pprint
from pyCentreon import pyCentreon

def main():
    api = pyCentreon.CentreonApi('https://centreon.example', 'clapi', 'clapitest')
    pprint(api.call("show", "downtime"))

if __name__ == '__main__':
    main()
