#!/usr/bin/python2

print("content-type:text/html")
import commands as sp


cmd= "sudo rpm -i /root/Desktop/jdk-8u171-linux-x64.rpm"
output=sp.getstatusoutput(cmd)
if output[0]==0:
	print("location:menule.py")
	print("")
else:
	print("")
	print("Error")
