#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import socket,gevent




def server(port):
    s = socket.socket()
    s.bind(("0.0.0.0",port))
    s.listen(500)
    while True:
        cli,addr = s.accept()
        gevent.spawn(handle_request,cli)


def handle_request(conn):
    try:
        while True:
            data = conn.revc(1024)
            print ("recv:",data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print (ex)
    finally:
        conn.close()

if __name__ == "__main__":
    server(8001)