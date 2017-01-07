#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

from multiprocessing import Process,Pipe



def f(conn):
    conn.send([42,None,'hello from child'])
    conn.close()






if __name__ == "__main__":
    parent_conn,child_conn = Pipe()
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()