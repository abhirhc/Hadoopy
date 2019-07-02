#!/usr/bin/python2

print("content-type:text/html")
import commands as sp


cmd=" sudo rpm -ivh /root/Desktop/hadoop-1.2.1-1.x86_64.rpm --force"
output=sp.getstatusoutput(cmd)
if output[0]==0:
	print("location:menule.py")
	print("")
else:
	print("")
	print("Error")
