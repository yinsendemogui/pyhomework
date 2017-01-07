#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

from multiprocessing import Process,Lock,Queue



def f():
    q = Queue()
    q.put(3)
    return q




if __name__ == "__main__":
    lock = Lock()
    # for num in range(100):
    p =Process(target=f)
    q = p.start()
    # p.join()
    print q.get()
