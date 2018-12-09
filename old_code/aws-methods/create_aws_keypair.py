import boto3

session = boto3.client(						#establish aws session
    service_name="ec2",
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name='us-east-1'
)
keypair = session.create_key_pair(KeyName='test')		# create a keypair
file = open('test.pem','w')
file.write(str(keypair['KeyMaterial']))					# store the file locally
file.close()

