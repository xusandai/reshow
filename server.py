#!/usr/bin/python3
# 文件名：server.py
# -*- coding: UTF-8 -*-
# 导入 socket、sys 模块

import socket
import sys
import time
import getpass
import read_file
import checksum
import bigEncode
import ParsBufLen


sz_src_file=open("../shhxzq_market_data//debug/sz_20170725.txt",'rb')


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
server_socket.settimeout(100)
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
logon=client_socket.recv(10240)
print("logon msg : ")
print(logon)

read_file.trans_data_sz(sz_src_file,client_socket)
# msg_type=sz_src_file.read(4)
# client_socket.send(bigEncode.bigEncode(msg_type,4))

# body_len=sz_src_file.read(4)
# client_socket.send(bigEncode.bigEncode(body_len,4))

# send_id=sz_src_file.read(20)
# client_socket.send(send_id)

# target_id=sz_src_file.read(20)
# client_socket.send(target_id)

# heart_beat_int=sz_src_file.read(4)
# client_socket.send(bigEncode.bigEncode(heart_beat_int,4))

# password=sz_src_file.read(16)
# client_socket.send(password)

# DefaultApplVerID=sz_src_file.read(32)
# client_socket.send(DefaultApplVerID)

# check_sum=sz_src_file.read(4)
# client_socket.send(bigEncode.bigEncode(check_sum,4))

#client_socket.send(sz_src_file.read(104))


# relogon=sz_src_file.read(104)
# print("relogon sendid : ")
# print(relogon[8:27])
# print("relogon recvid : ")
# print(relogon[28:47])
# client_socket.send(relogon)
# i=0
# while True:
# 	if not read_file.trans_data_sz(sz_src_file,client_socket):
# 		print("ShenZhen market end!")
# 		break
# 	i=i+1
# 	print(i)
	#print(i)
#	sh_dest_file=open("/home/"+user_name+"/mnt/local/SHSZ/FAST/mktdt00.txt",'wb+') 
#	if not read_file.trans_data_sh(sh_src_file,sh_dest_file):
#		print("ShangHai market end!")
	#time.sleep(1)

#	sh_dest_file.close()
