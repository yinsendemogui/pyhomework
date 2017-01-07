#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：


import threading,time


event = threading.Event()

def lighter():
    count = 0
    while True:
        if count > 10 and count <= 20:  # 改成红灯
            event.clear() #把标志位清空
            print "\033[41;1m红灯已经开启！\033[0m",count
        elif count > 20:
            event.set() #变绿灯
            count = 0
        else:
            print "\033[46;1m绿灯已经开启！\033[0m",count
            event.set()
        time.sleep(1)
        count += 1

def car(name):
    time.sleep(1)
    while True:
        if event.is_set(): #如果设置了标志位
            print "running...{0}".format(name)
            time.sleep(1)
        else:
            print "see red light,waiting..."
            event.wait()
            print "绿灯已经打开，start going...{0}".format(name)

light = threading.Thread(target=lighter)
light.start()

car1 = threading.Thread(target=car,args=('奔驰',))
car1.start()

