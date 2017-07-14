#!/usr/bin/python3
# 文件名：server.py
# -*- coding: UTF-8 -*-
# 导入 socket、sys 模块

import socket
import sys
import time
import getpass
import read_file
# 创建 socket 对象
server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 获取本地主机名
host = "127.0.0.1"
port = 12345
user_name=getpass.getuser()

# 绑定端口
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

# 建立客户端连接
client_socket,addr = server_socket.accept()      
print("连接地址: %s" % str(addr))
#receive logon message from seed

msg={}
msg['type']=client_socket.recv(4)
msg['body_length']=client_socket.recv(4)
msg['body']=client_socket.recv(int.from_bytes(msg['body_length'],byteorder='big'))
msg['end']=client_socket.recv(4)
#set file paths
sh_src_file=open("/home/"+user_name+"/hxzq/market_data/bin/debug/sh_2017-02-07.txt",'rb') 
sz_src_file=open("/home/"+user_name+"/hxzq/market_data/bin/debug/sz_2017-02-06.txt",'rb')

while True:
	if not read_file.trans_data_sz(sz_src_file,client_socket):
		print("ShenZhen market end!")
	sh_dest_file=open("/home/"+user_name+"/mnt/local/SHSZ/FAST/mktdt00.txt",'wb+') 
	if not read_file.trans_data_sh(sh_src_file,sh_dest_file):
		print("ShangHai market end!")
	time.sleep(3)

	sh_dest_file.close()
