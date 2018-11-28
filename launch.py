#create a Amzon Linux Image
import re
import time
import boto3
import json
import os
import sys
import mysql.connector
from datetime import datetime, timedelta
import string
import random
from subprocess import call

def id_generator(size=12, chars=string.ascii_letters):
	return ''.join(random.choice(chars) for _ in range(size))


#takes one argument from console
requested_user = sys.argv[1]
#instance user name for amazon is 
instance_username = "ec2-user"
instance_password = id_generator();
ec2 = boto3.resource('ec2')
mydb = mysql.connector.connect(host="localhost",user="vcluser",passwd="nbv_12345",database="vcl")
mycursor = mydb.cursor()

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-013be31976ca2c322',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='aws-ec2-keypair'
 )

#by default there are only 1 hour reservation
instance_ID = instances[0].id
time.sleep(20)

aws_cmd = "aws ec2 describe-instances --instance-ids " + instance_ID + " --query 'Reservations[].Instances[].PublicDnsName'"
output = os.popen(aws_cmd).read()
matchObj = re.match( r'\[\s+"(\S+)"',output,re.M|re.I)
if matchObj:
	instance_dns = matchObj.group(1)

ssh_cmd = "ssh -i \"aws-ec2-keypair.pem\" "+ instance_username + "@" + instance_dns + " \"printf \"" + instance_password + "\" | sudo passwd " + instance_username + "  --stdin;sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config;sudo service sshd restart\"" 

os.system(ssh_cmd)

#print type(instances[0].id)
print instance_ID
start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#end time will after 1 hour
end_time = datetime.now() + timedelta(hours=1);
sql = "INSERT INTO aws_reservation (instance_id,username,start_time,end_time,daterequested,instance_username,password,dns_ip) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
val = (instance_ID,requested_user,start_time,end_time,start_time,instance_username,instance_password,instance_dns)
mycursor.execute(sql, val)
mydb.commit()

