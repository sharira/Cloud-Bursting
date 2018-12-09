#!/usr/bin/python


import cgi, cgitb 
import os
import commands
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('username')
duration  = form.getvalue('duration')

#username = "admin"
#duration  = "60"
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print os.getuid()
print "<h2>Hello %s %s</h2>" % (username, duration)
python_str = "python launch.py "+username+" "+duration
result = commands.getoutput(python_str)
print result
print "</body>"
print "</html>"

