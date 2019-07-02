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
ipnj=cmd.getvalue("ipnj")



ff=open("/hadoop/mapred-site.xml","w")
ff.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>

</configuration>""".format(ipnj))
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


s.getoutput("sudo sshpass -p {} scp -o StrictHostKeyChecking=no /hadoop/mapred-site.xml {}@{}:/etc/hadoop/mapred-site.xml".format(password,user,ipnj))
s.getoutput("sudo sshpass -p {} scp -o StrictHostKeyChecking=no /hadoop/core-site.xml {}@{}:/etc/hadoop/core-site.xml".format(password,user,ipnj))
s.getoutput(" sudo rm -r /hadoop/mapred-site.xml")
s.getoutput("sudo rm -r /hadoop/core-site.xml")
s.getoutput(" sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} iptables -F ".format(password,user,ipnj))
s.getoutput(" sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} hadoop-daemon.sh start jobtracker".format(password,user,ipnj))
f=s.getoutput(" sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} jps | grep JobTracker".format(password,user,ipnj))
if f==(""):
	print("")
	print("Need more work :)")
else:
	print("location:menule.py")
	print("")
		
