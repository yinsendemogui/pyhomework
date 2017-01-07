#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import select
import socket
import sys
import Queue


server = socket.socket()
server.bind(('localhost',9000))
server.listen(1000)
server.setblocking(False) #设置成不阻塞模式



inputs = [server,]
outputs = []
msg_dic = {}
while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)
    print (readable,writeable,exceptional)
    for r in readable:
        if r is server:   #来了一个新链接
            conn,addr = server.accept()  #非阻塞模式，没有链接过来就会报错
            print "来了个新链接",addr
            inputs.append(conn)  # 因为这个新建立的链接还没发数据过来，现在就直接conn.accept()就会报错-->非阻塞
            #所以要想实现这个客户端发数据来时server端能知道，那就需要让select再此检测这个链接
            msg_dic[conn] = Queue.Queue()  #初始化一个队列，后面存要返回给这个客户端的数据
        else:
            data = r.recv(1024)
            print "收到数据：",data
            msg_dic[r].put(data)
            outputs.append(r)


    for w in writeable:
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)
        outputs.remove(w)


    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)


