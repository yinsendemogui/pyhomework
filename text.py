#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import select
import socket
import Queue

s = socket.socket()
s.bind(('localhost',9000))
s.listen(1000)
s.setblocking(False)

inputs = [s,]
outputs = []
msg_dic = {}

while True:
    readable,writable,exceptional = select.select(inputs,outputs,inputs)
    for r in readable:
        if r is s:
            conn,addr = s.accept()
            inputs.append(conn)
            msg_dic[conn] = Queue.Queue()
        else:
            data = r.recv(1024)
            print (data)
            outputs.append(r)
            msg_dic[r].put(data)
    for w in writable:
        data = msg_dic[w].get()
        w.sendall(data)
        outputs.remove(w)
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)





