import boto3

session = boto3.Session(						#establish aws session
                aws_access_key_id="",
                aws_secret_access_key="",
                region_name='us-east-1'
        )
ec2 = session.resource('ec2')

instance_list = ['i-0a9386173f7d002d7']						#give the instance ID
ec2.instances.filter(InstanceIds=instance_list).stop()
ec2.instances.filter(InstanceIds=instance_list).terminate()		#terminate the instance
