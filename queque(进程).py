

from multiprocessing import Process,Queue

import threading



def f():
    q.put([42,None,'hello'])
    # print(q.get())


if __name__=='__main__':
    q = Queue()
    p = Process(target=f)
    # p = threading.Thread(target=f,args=(q,))
    p.start()
    print(q.get())

