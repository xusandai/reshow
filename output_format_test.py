#!/usr/bin/python3
#file name: output_format_test.py

file=open("../../hxzq/test/sz_2016_11_01.txt",'rb')
output=file.read(4)
print(output+"q")
print("{:x}".format("a"))
