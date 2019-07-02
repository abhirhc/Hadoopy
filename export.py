#!/usr/bin/python2

print("content-type:text/html")
import commands as sp


cmd="sudo bash -c 'echo export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/ >> /root/.bashrc ; echo export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH >> /root/.bashrc'"
output=sp.getstatusoutput(cmd)
if output[0]==0:
	print("location:menule.py")
	print("")
else:
	print("")
	print("Error")
