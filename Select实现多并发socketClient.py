#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import socket

client = socket.socket()

client.connect(('localhost',9000))


while True:
    choose = raw_input(">>:")
    client.sendall(choose)
    data = client.recv(1024)
    print (data)

client.close()