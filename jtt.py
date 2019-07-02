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
ipnj=cmd.getvalue("ipnj")
ipnt=cmd.getvalue("ipnt")



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

s.getoutput("sudo sshpass -p {} scp -o StrictHostKeyChecking=no /hadoop/mapred-site.xml {}@{}:/etc/hadoop/mapred-site.xml".format(password,user,ipnt))
s.getoutput(" sudo rm -r /hadoop/mapred-site.xml")
s.getoutput(" sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} iptables -F ".format(password,user,ipnt))
s.getoutput(" sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} hadoop-daemon.sh start tasktracker".format(password,user,ipnt))
f=s.getoutput(" sudo sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{} jps | grep TaskTracker".format(password,user,ipnt))
if f==(""):
	print("")
	print("Need more work :)")
else:
	print("location:menule.py")
	print("")
		
