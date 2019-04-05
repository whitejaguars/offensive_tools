#!/usr/bin/env python
import os, sys
import dependencies.http_handler as http_handler

if not len(sys.argv)==3:
    print 'Usage: proxy_autonav.py url_file proxy'
    exit(0)

def main():
    #proxies = urllib2.urlopen('http://rmccurdy.com/scripts/proxy/good.txt').read().splitlines()
    #proxy = randomproxy(proxies)
    proxy = str(sys.argv[2])
    filename = str(sys.argv[1])
    if not os.path.isfile(filename):
        print 'WhiteJaguars'
        print 'This script basically navegate the URLs provided sending them to a proxy'
        print 'Why ? because it\'s an easy way to add sites to tools like Burp or ZAP'
        print 'Usage: proxy_autonav.py url_file proxy'
        exit()

    print 'Using Proxy: '+proxy

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    efile = open(filename,'r').read()
    lines = efile.split('\n')
    i = 1
    for url in lines:
        if len(url) > 7:
            if url[:7] == 'http://' or url[:8] == 'https://':
                try:
                    response = http_handler.send(url = str(url), headers = headers, proxy = proxy)
                    print '['+str(i)+' of '+str(len(lines))+'] '+url
                except:
                    pass
        i+=1

if __name__ == '__main__':
    main()
    print 'Process completed'
