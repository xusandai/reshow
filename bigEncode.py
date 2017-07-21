#!/usr/bin/python3
# 文件名：bigEncode.py
def bigEncode(buf, len):
    buf2=bytearray(buf)
    for i in range(len):
        buf2[i]=buf[len-1-i]
    return buf2