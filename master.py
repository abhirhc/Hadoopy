#!/usr/bin/python36
print("content-type:text/html")
import subprocess as sp
import cgi
import cgitb
cgitb.enable()
#for hdfs-site.xml.........................................................................
cmd=cgi.FieldStorage()
user=cmd.getvalue("user")
password=cmd.getvalue("password")
ipn=cmd.getvalue("ipn")
na=open("/hadoop/hdfs-site.xml","w")
na.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/name</value>
</property>

</configuration>""")
na.close()
nc=open("/hadoop/core-site.xml","w")
nc.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>\n""")
nc.write("<value>hdfs://{}:9001</value>\n".format(ipn))
nc.write("</property>\n")
nc.write("</configuration>")
nc.close()

sp.getoutput("sudo sshpass -p {} scp -o StrictHostKeyChecking=no /hadoop/hdfs-site.xml {}@{}:/etc/hadoop/hdfs-site.xml".format(password,user,ipn))
sp.getoutput("sudo sshpass -p {} scp -o StrictHostKeyChecking=no /hadoop/core-site.xml {}@{}:/etc/hadoop/core-site.xml".format(password,user,ipn))
sp.getoutput("sudo rm -r /hadoop/hdfs-site.xml")
sp.getoutput("sudo rm -r /hadoopo/core-site.xml")
sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} mkdir /name".format(password,user,ipn))
sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} hadoop namenode -format -force".format(password,user,ipn))
sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} iptables -F".format(password,user,ipn))
sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} hadoop-daemon.sh start namenode".format(password,user,ipn))
f=sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} jps | grep NameNode".format(password,user,ipn))
if f==(""):
	print("")
	print("Need more work :(")
else:
	print("location:menule.py")
	print("")


	
