import boto3
import json

session = boto3.Session(			# establish aws session
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name='us-east-1'
)

ec2instances = {}
ec2 = session.resource('ec2')			# get the running instances
running_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name','Values': ['running']}])

for instance in running_instances:		#for all instances get the instance details
    name = 'nothing'
    ec2instances[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Private IP': instance.private_ip_address,
        'Public IP': instance.public_ip_address,
        }
print json.dumps(ec2instances)			#print the json format of the details

