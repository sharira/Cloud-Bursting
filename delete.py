#!/usr/bin/env python
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
import json

#takes one argument from console
instance_id = sys.argv[1]

print "delete called " + instance_id

with open('aws_config.json') as f:
	 data = json.load(f)

session = boto3.Session(region_name=str(data['region_name']),aws_access_key_id=str(data['aws_access_key_id']),aws_secret_access_key=str(data['aws_secret_access_key']),
	aws_session_token=str(data['aws_session_token']))

ec2 = session.resource('ec2')
instance_list = instance_id.split()
ec2.instances.filter(InstanceIds=instance_list).stop()
ec2.instances.filter(InstanceIds=instance_list).terminate()

mydb = mysql.connector.connect(host="localhost",user="vcluser",passwd="nbv_12345",database="vcl")
mycursor = mydb.cursor()

sql = "delete from aws_reservation where instance_id = '" + instance_id + "'"
mycursor.execute(sql)
mydb.commit()
