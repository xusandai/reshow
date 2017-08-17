#!/usr/bin/python3
# 文件名：server.py
# -*- coding: UTF-8 -*-
# 导入 socket、sys 模块

import socket
import sys
import time
import getpass
import read_file
import threading


sz_src_file = '/home/xhw/shhxzq_market_data/debug/sz_20170802.txt.backup'

#sz_src_file=open("../shhxzq_market_data/debug/test_data.backup",'rb')
#print(sz_src_file.read(8))
# for i in range(10000000):
# 	len = header[i+4] *256^3 +header[i+5] *256^2+header[i+6] *256^1+header[i+7] *256^0
# 	sum = header[i+100] *256^3 +header[i+101] *256^2+header[i+102] *256^1+header[i+103] *256^0
# 	if (checksum.checksum(header[i:i+100], 100, sum)):
# 		position = i
# 		print(i)
# 		break
# print(position)    	
# 创建 socket 对象
server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.settimeout(1000)
# 获取本地主机名
host = "127.0.0.1"
port = 12345
user_name=getpass.getuser()

# 绑定端口
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

client_sockets = []
client_count = 0
threads = []
i=0
sh_src_file=open("/home/xhw/shhxzq_market_data/debug/sh_20170808.txt",'rb')
client_socket, addr = server_socket.accept()
print(client_socket,addr)
read_file.trans_data_sh(sh_src_file,client_socket)

# class socket_thread (threading.Thread):

     

#     def __init__(self, server_socket, sz_src_file):
#         threading.Thread.__init__(self)		
#         self.__server_socket = server_socket
#         self.__sz_src_file = open(sz_src_file,'rb')

#     def run(self):
#         self.__client_socket = self.__server_socket.accept()
#         print("connect addr : %s" % str(self.__client_socket[0]))
#         socket_thread(server_socket,sz_src_file).start()
#         read_file.trans_data_sz(self.__sz_src_file,self.__client_socket[0])
#         self.__client_socket[0].close()

# socket_thread(server_socket,sz_src_file).start()
# time.sleep(3)
# socket_thread(server_socket,sz_src_file).start()
