#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：
import gevent,time
import urllib2
from gevent import monkey

monkey.patch_all()   #把当前程序的所有io操作给我单独的做上标记，如此一来，gevent才能发现io操作进行自动协程，如果不加gevent发现不了，因此还是串行同步

def F(url):
    print ("GET:%s" % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print (len(data))
    # f = open("url.html","wb")
    # f.write(data)
    # f.close()
    # print ("%d bytes received from %s." % (len(data),url))

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(F,"https://www.python.org/"),
    gevent.spawn(F,"https://www.yahoo.com/"),
    gevent.spawn(F,"https://www.sina.com/"),
])
print "异步cost：",time.time() - async_time_start

time_start = time.time()
urls = ["https://www.python.org/",
        "https://www.yahoo.com/",
        "https://www.sina.com/"
        ]

for url in urls:
    F(url)
print "同步cost：",time.time() - time_start