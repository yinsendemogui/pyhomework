#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import Queue

# q = Queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)

q = Queue.PriorityQueue()
q.put((5,"alex"))
q.put((5,"chensiqi"))
q.put((5,"sdfsd"))
q.put((5,"xxx"))
print q.get()
print q.get()
print q.get()
print q.get()
