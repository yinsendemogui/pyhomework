#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

from multiprocessing import Process,Pool,Lock

import time
import os



def Foo(i):
    time.sleep(2)

    print ("in process",os.getpid())

    return i+100



def Bar(arg):
    print ("-->exec done:",arg)




if __name__=="__main__":
    pool = Pool(3) #允许进程池里同时放入5个进程

    for i in range(10):
        # pool.apply(func=Foo,args=(i,))  #串行执行
        # pool.apply_async(func=Foo,args=(i,))  #并发执行
        pool.apply_async(func=Foo,args=(i,),callback=Bar)  #callback=回调（前边执行完毕再执行callback）



print ('end')
pool.close()
pool.join()  #如果要等所有进程结束，再关闭所有进程池，那么必须先close，再join