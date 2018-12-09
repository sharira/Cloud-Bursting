import mysql.connector as mariadb
import datetime
import os

base_str = "python aws_delete.py "
mariadb_connection = mariadb.connect(host="localhost",user="vcl_admin",passwd="Admin123~",database='vcl')
cursor = mariadb_connection.cursor()
cursor.execute("SELECT instance_id,end_time FROM aws_reservation")
curr_date = datetime.datetime.now()
for id,end in cursor:
#        print(id,str(end))
        if curr_date > end:
		cmd_str= base_str + str(id)
		os.system(cmd_str)
        	        

