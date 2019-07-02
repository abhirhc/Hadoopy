#!/usr/bin/python2

print("content-type:text/html")
print("")


print("<strong><marquee>MaStEr ParLouR</strong></marquee>")
print("<b>Authenticate yourself<b>")
print("<form action='master.py'>")
print("""
<table border = 3>
<tr>
<td>EnterTheNameOfUser</td>
<td><input type="text"  name="user" /></td>
</tr>
<tr>
<td>EnterThePassword</td>
<td><input type="password" name="password" />
</tr>
<tr>
<td>Enter the ip of namenode</td>
<td><input type="text" name="ipn" /></td>
</tr>
<td>submit</td>
<td><input type="submit" />
</tr>
</table>""")
print("</form>")
