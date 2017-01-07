#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：


import threading
import time




# def run(n):
#     lock.acquire()
#     global num
#     print ("结束！{0},{1}".format(n,threading.current_thread()))
#     num +=1
#     lock.release()

def run(n):
    semaphore.acquire()
    time.sleep(1)
    global num
    num +=1
    print ("结束{0},{1}".format(num,threading.activeCount()))
    semaphore.release()



if __name__ == "__main__":
    num = 0
    # lock = threading.RLock()
    semaphore = threading.BoundedSemaphore(5)
    for i in range(50):
        t = threading.Thread(target=run,args=(i,))
        # t.setDaemon(True)
        t.start()


    while threading.activeCount() != 1:
        pass
    else:
        print ("num:",num)

