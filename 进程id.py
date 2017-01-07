#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

from multiprocessing import Process
import os


def info(title):
    print (title)
    print ("module name:",__name__)
    print ("parent process",os.getppid())
    print ("process id:",os.getpid())
    print ("\n\n")




if __name__ == "__main__":
    info("\033[32:1mmain process line\033[0m")
    p = Process(target=f,args=('bob',))
    p.start()
    p.join()
