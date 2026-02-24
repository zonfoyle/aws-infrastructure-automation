"""
This script manages Amazon EC2 instances using the Boto3 Python SDK.
"""
# import statements
import boto3

# create ec2 resource and instance name
ec2 = boto3.resource('ec2', region_name='us-east-1')
instance_name = 'dct-ec2-hol'

# store instance id
instance_id = None

# check if instance already exists and hasn't been terminated
instance_exists = False
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 
              'Values': ['pending', 'running', 'stopping', 'stopped']}]
)

for instance in instances:
    if instance.tags:
        for tag in instance.tags:
            if tag['Key'] == 'Name' and tag['Value'] == instance_name:
                instance_exists = True
                instance_id = instance.id
                print(f"Instance {instance_name} already exists with ID: {instance_id}")
                break
    if instance_exists:
        break

# Launch a new EC2 instance if it hasn't already been created
if not instance_exists:
    new_instance = ec2.create_instances(
        ImageId='ami-0f3caa1cf4417e51b',
        MinCount=1,
        MaxCount=1,
        InstanceType='t3.micro',
        KeyName='us-east-kp',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    }
                ]
            }
        ]
    )
    instance_id = new_instance[0].id
    print(f"Launched EC2 instance with ID: {instance_id}")

# Stop an instance
def stop_instance(instance_id):
    instance = ec2.Instance(instance_id)
    instance.stop()
    print(f"Stopping instance: {instance_id}")

# Start an instance
def start_instance(instance_id):
    instance = ec2.Instance(instance_id)
    instance.start()
    print(f"Starting instance: {instance_id}")

# Terminate an instance
def terminate_instance(instance_id):
    instance = ec2.Instance(instance_id)
    instance.terminate()
    print(f"Terminating instance: {instance_id}")

# Test the functions
terminate_instance(instance_id)