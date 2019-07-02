#!/usr/bin/python36
print("content-type:text/html")
import subprocess as s
import cgi
import cgitb
cgitb.enable()
#for hdfs-site.xml.........................................................................
cmd=cgi.FieldStorage()
user=cmd.getvalue("user")
password=cmd.getvalue("password")
ipn=cmd.getvalue("ipn")
ipnd=cmd.getvalue("ipnd")



ff=open("/hadoop/hdfs-site.xml","w")
ff.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/slaves</value>
</property>

</configuration>""")
ff.close()
#for core-site.xml ...................................................

fh=open("/hadoop/core-site.xml","w")
fh.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>\n""")
fh.write("<value>hdfs://{}:9001</value>\n".format(ipn))
fh.write("</property>\n")
fh.write("</configuration>")
fh.close()

s.getoutput("sudo sshpass -p {} scp -o StrictHostKeyChecking=no /hadoop/hdfs-site.xml {}@{}:/etc/hadoop/hdfs-site.xml".format(password,user,ipnd))
s.getoutput(" sudo sshpass -p {} scp -o StrictHostKeyChecking=no /hadoop/core-site.xml {}@{}:/etc/hadoop/core-site.xml".format(password,user,ipnd))
s.getoutput(" sudo rm -r /hadoop/hdfs-site.xml")
s.getoutput(" sudo rm -r /hadoop/core-site.xml")
s.getoutput(" sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} iptables -F ".format(password,user,ipnd))
s.getoutput(" sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} hadoop-daemon.sh start datanode".format(password,user,ipnd))
f=s.getoutput(" sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} jps | grep DataNode".format(password,user,ipnd))
if f==(""):
	print("")
	print("Need more work :)")
else:
	print("location:menule.py")
	print("")
		
