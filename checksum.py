#!/usr/bin/python3
# 文件名：checksum.py
# -*- coding: UTF-8 -*-
def checksum(data, len, sum):
    sumed=0
    for i in range(len):
        sumed=sumed+data[i]
    print(sumed%256,sum)
    if (sumed%256 == sum):
        
        return True
    return False