#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：

import paramiko

transport = paramiko.Transport(('chensiqi',22))
transport.connect(username = 'root',password='csq122600')

sftp = paramiko.SFTPClient.from_transport(transport)
#将文件 上传服务器
# sftp.put(本地路径，服务器路径)
sftp.put('/Users/chensiqi/Git/Alex/LessonFour/ReadMe.pdf','/root/ReadMe.pdf')
#将文件 下载到本地
# sftp.get(服务器路径，本地路径)

transport.close()

