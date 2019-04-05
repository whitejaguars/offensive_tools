#!/usr/bin/env python
import sys
import dependencies as crawler


if not len(sys.argv)==3:
    print 'WhiteJaguars Cyber Security'
    print 'This is an easy way for getting plaform information from Web Servers'
    print 'returning the Server header, application server and Development framework'
    print ' '
    print 'Usage: platform_check.py url proxy'
    exit(0)


def main():
    #proxies = urllib2.urlopen('http://rmccurdy.com/scripts/proxy/good.txt').read().splitlines()
    #proxy = randomproxy(proxies)
    proxy = str(sys.argv[2])
    url = str(sys.argv[1])
    print 'URL: ' + url
    print 'Using Proxy: '+proxy
    serverinfo = crawler.get_platform_info(url, proxy)
    if serverinfo is not None:
        print 'Server: ' + serverinfo['Server']
        print 'Application Server: '+ serverinfo['AppServer']
        print 'Development Language: ' + serverinfo['Language']


if __name__ == '__main__':
    main()
    print 'Process completed'
