#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#file name : read_file.py
import sys
import getpass
import time
import os
import checksum
import ParsBufLen



def read_sz(src_file):
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
    eof = len(msg_type) < 4 
    msg={'msg_type':msg_type,
         'msg_type_value':msg_type_value,
		 'body_len':body_len,
		 'body_len_value':body_len_value,
		 'body':body,
         'actual_body_len_value' : len(body),
		 'tail':tail,
		 'tail_value':tail_value,
		 'data':data,
         'eof':eof}
    return msg

#read source data of ShenZhen and transport it to seed
def trans_data_sz(src_file,client_socket):
    i = 0
    while True:
        msg=read_sz(src_file)	 
 
        if msg:       #判断body_length是否超长           	
            #if msg['msg_type']: 
            if not msg['eof']: #判断文件是否结束            
                if checksum.checksum(msg['data']):
                    client_socket.send(msg['data'])	
                    
                    if i == 0:
                        print(msg['data'])
                        print(src_file.tell())
                    i += 1		
                elif (msg['body_len_value'] == msg['actual_body_len_value']):
                    #print("body_len : ",msg['body_len_value'])
                    src_file.seek(-msg['body_len_value']-11,1)
                else:
                    src_file.seek(-msg['actual_body_len_value']-7,1)
            else:
                print("Shenzhen market file end!")
                print(msg)
                break
        else:
            src_file.seek(-7,1)

def get_domin(src_file):
    tmp = b''
    begin_string = b''
    while b'\x01' != tmp:      
        tmp = src_file.read(1) 
        begin_string += tmp
    
    return begin_string
def compute_value(buf):
    result = 0
    bit_len = len(buf)
    for i in range(bit_len):
        result += (buf[bit_len-i-1]-48)*10**i
    return result

def read_sh(src_file):
    tmp = bytearray(src_file.read(1024))
    position = tmp.find(b'8=STEP')
    i = 0
    while not position: 
        i += 1
        tmp = bytearray(src_file.read(1024))
        position = tmp.find(b'8=STEP')
    if 1024 < i:
        msg['eof'] = True
        return msg
    src_file.seek(position-1024,1)
    begin_string = get_domin(src_file)
    body_len = get_domin(src_file)
    body_len_value = compute_value(body_len[2:len(body_len)-1])
    if body_len_value > 1024000:
        src_file.seek(-len(body_len),1)
        return False
    body = src_file.read(body_len_value)
    tail = get_domin(src_file)
    
    if b'10=' != tail[:3]:
        src_file.seek(-len(body_len)-len(tail),1)
        return False

    msg={'begin_string':begin_string,
         'body_len':body_len,
		 'body_len_value':body_len_value,
		 'body':body,
		 'tail':tail,
         'eof':False}
    return msg

    

#read source data of shanghai and transport it to seed
def trans_data_sh(src_file,client_socket):	
    while True:
        msg = read_sh(src_file)
        if msg:
            if msg['eof']:
                print('shanghai market end !')
                break
            print(msg['begin_string']+msg['body_len']+msg['body']+msg['tail'])
            client_socket.send(msg['begin_string']+msg['body_len']+msg['body']+msg['tail'])
        
