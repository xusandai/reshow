#!/usr/bin/python3
#file_name test.py
# -*- coding: UTF-8 -*-
# 导入 socket、sys 模块

import socket
import sys 
import time
import getpass
import read_file
import os

last_access_time=os.stat("server.py").st_atime
if time.time()-last_access_time>100000:
	print('yes')
else:
	print("no  ",last_access_time)
