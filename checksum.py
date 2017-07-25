#!/usr/bin/python3
# 文件名：checksum.py
# -*- coding: UTF-8 -*-

def checksum(msg):
    msg_len=len(msg)
    sumed=0
    sum=int.from_bytes(msg[msg_len-4:msg_len],'big')
    for i in range(msg_len-4):
        sumed=sumed+msg[i]
    #print(sumed%256,sum)
    if (sumed%256 == sum):       
        return True
    return False