#!/bin/python

import cgi,cgitb
import commands
form = cgi.FieldStorage()

instance = form.getvalue('id')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Delete CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s</h2>" % (instance)
#$tmp = os.system('./test.py')
python_str = "python aws_delete.py "+instance
#result = commands.getoutput("python test.py username duration")
result = commands.getoutput(python_str)
print result
print "</body>"
print "</html>"
