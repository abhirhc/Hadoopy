#!/usr/bin/python2

print("content-type:text/html")
print("")
import commands as sp

java="rpm -q jdk1.8"
output_java=sp.getstatusoutput(java)
if output_java[0]==0:
	java_status_check="installed"
else:
	java_status_check="not installed"

 
cmd="rpm -q hadoop"
output=sp.getstatusoutput(cmd)
if output[0]==0:
	Hadoop_status_check="installed"
else:
	Hadoop_status_check="not installed"

print("<strong>HADOOP STATION</strong>")
print("""
<table border=4>
<tr>
<td>Java Meter</td>
<td>{}</td>
</tr>
<tr>
<td>JAVA FUEL FILLING</td>
<td><a href="javainstall.py">Click Here to install</a></td>
</tr>
<tr>
<td>Java Exports</td>
<td><a href="export.py">Click here to export</a></td>
</tr>
<tr>
<td>HAdOOp SoFtWaRE CHecKuP</td>
<td>{}</td>
</tr>
<tr>
<td>Hadoop software install</td>
<td><a href="hadoopinstall.py">Click Here to install</a></td>
</tr> 
<tr>
<td>Master Parlour</td>
<td><a href="masterform.py">Click here</td>
</tr>
<tr>
<td>Slave Parlour</td>
<td><a href="datanode.py">click here</td>
</tr>
<tr>
</table> <br />""".format(java_status_check,Hadoop_status_check))

print("<strong>CoMpUtInG ZoNe</strong>")
print("""<table border =3>
<tr>
<td>JobTracker</td>
<td><a href="job.py">Click HERE</a></td>
</tr>
<tr>
<td>TaskTracker</td>
<td><a href="jt.py">Click HERE</a></td>
</tr>
</table>
""")
