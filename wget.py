#!/usr/bin/python

import sys, getopt
from httplib2 import Http

def main(argv):
    wp_url = ''
    try:
        opts, args = getopt.getopt(argv,"hu:",["url=",])
    except getopt.GetoptError:
        print 'wget.py -u <url>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'simple_wget.py -u <url>'
            sys.exit()
        elif opt in ("-u", "--url"):
            wp_url = arg
    if wp_url == '':
        wp_url = raw_input('Type the URL:')
    if wp_url != '':
        h = Http()
        print '**********************************************'
        print '* Simple Script for getting http content     *'
        print '* WhiteJaguars.com                           *'
        print '* Use this if not able to use wget or curl   *'
        print '**********************************************'

        resp, content = h.request(wp_url, "GET", '')
        print content

    else:
        print 'wget.py -u <url>'
if __name__ == "__main__":
   main(sys.argv[1:])
