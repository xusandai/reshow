#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#file name : read_file.py
import sys
import getpass
import time
import os
#read source data of ShenZhen and transport it to seed
def trans_data_sz(src_file,client_socket):
	msg_type=src_file.read(4)
	#print('msg_type',msg_type)
	if not msg_type:
		#print('msg_type',msg_type)
		return False
	body_length=src_file.read(4)
	body=src_file.read(int.from_bytes(body_length,byteorder='big'))
	check_sum=src_file.read(4)
	client_socket.send(msg_type+body_length+body+check_sum)                                         
	return True

#read source data of shanghai and transport it to seed
def trans_data_sh(src_file,dest_file):	
	#src_file and dest_file are returned by open() 
	#print(`time.time())
	last_access_time=os.stat(dest_file.name).st_atime
	begin_str=src_file.read(7)
	if not begin_str:
		return False
	#print(os.stat(dest_file.name).st_atime,'  ',begin_str)
	version=src_file.read(9)
	body_length=src_file.read(11)
	real_body_length=0
	i=0
	for i in range(10):
		if body_length[i]!=0x20:
			real_body_length=real_body_length*10+int(body_length[i])-0x30
		i+=1
	#print("body length ",real_body_length)
	body=src_file.read(real_body_length)
	access_time=os.stat(dest_file.name).st_atime
	dest_file.write(begin_str+version+body_length+body)
	return True
