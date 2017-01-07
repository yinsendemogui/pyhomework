#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：
import time,threading
import multiprocessing


def thread_run():
    print (threading._get_ident())


def run(name):
    time.sleep(2)
    print ("hello",name)
    t = threading.Thread(target=thread_run,)
    t.start()


if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run,args=('bob%s' %i,))
        p.start()
        #p.join()