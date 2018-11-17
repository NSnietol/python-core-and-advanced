'''
Created on Nov 17, 2018

@author: nilson.nieto
'''
import urllib.request as rq
import urllib

try:
    url = rq.urlopen('https://www.python.org')
    content = url.read()
    url.close()
    
except urllib.error.HTTPError:
    print('Page is not found')

f = open('python.html','wb')
f.write(content)
f.close()