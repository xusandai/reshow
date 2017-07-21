#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#file name : read_file.py
import sys
import getpass
import time
import os
import checksum
import ParsBufLen



def read_msg(src_file):
    msg_type=src_file.read(4)
    msg_type_value=int.from_bytes(msg_type,'big')

    body_len=src_file.read(4)
    body_len_value=int.from_bytes(body_len,'big')
    if body_len_value > 1024000:
        return False	
    body=src_file.read(body_len_value)

    tail=src_file.read(4)
    tail_value=int.from_bytes(tail,'big')
    data=bytearray(msg_type+body_len+body+tail)	
    msg={'msg_type':msg_type,
         'msg_type_value':msg_type_value,
		 'body_len':body_len,
		 'body_len_value':body_len_value,
		 'body,tail':body,
		 'tail':tail,
		 'tail_value':tail_value,
		 'data':data}
    return msg

#read source data of ShenZhen and transport it to seed
def trans_data_sz(src_file,client_socket):
    buf_len=src_file.read(8)
    buf_len_value=ParsBufLen.ParseBufLen(buf_len)
	
    #msg=read_msg(src_file)
    total_lost=0
    while True:
        msg=read_msg(src_file)		
        if msg: 
            if checksum.checksum(msg['data']):
                client_socket.send(msg['data'])			
            else:
                src_file.seek(-msg['body_len_value']-11,1)
        else:
    	    src_file.seek(-7,1)
      
    

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
