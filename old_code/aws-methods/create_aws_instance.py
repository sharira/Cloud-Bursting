import boto3
import time

session = boto3.Session(			#establish a AWS session
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name='us-east-1'
)

#ec2 = boto3.client('ec2')
ec2 = session.resource('ec2')
instance = ec2.create_instances(			#create an instance
        ImageId='ami-467ca739',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName="test_keypair2",			# create it using the keypair
        )
print("instances are created")
time.sleep(40)								#wait for some time for ec2 to get IP address
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])		# filter to see the running instances
for instance in instances:
    if instance.id == instance.id:
        print (instance.id,instance.public_ip_address)			# Print the public IP address
