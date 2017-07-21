#!/usr/bin/python3
# 文件名：data_filter.py
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


sz_src_file=open("../shhxzq_market_data/debug/sz_20170719.txt.from217",'rb')
#sz_target_file=open("../shhxzq_market_data/debug/sz_20170719.txt.from217.backup",'ab+')
len_buf_=sz_src_file.read(8)
msg_len=ParsBufLen.ParseBufLen(len_buf_)
msg=sz_src_file.read(msg_len)
body_len=int.from_bytes(msg[4:8],'big')
print(msg)
print(body_len)
while checksum.checksum(msg,msg_len):
    len_buf_=sz_src_file.read(8)
    msg_len=ParsBufLen.ParseBufLen(len_buf_)
    msg=sz_src_file.read(msg_len)
    body_len=int.from_bytes(msg[4:8],'big')

print(msg)