#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：


import paramiko

# （创建SSH对象）
ssh = paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='chensiqi',port=22,username='root',password='csq122600')
#执行命令
stdin,stdout,stderr = ssh.exec_command('ls')
#获取命令结果
result = stdout.read()
error = stderr.read()
print (result)
print (error)
#关闭连接
ssh.close()
