import boto3

client = boto3.client('ec2')
response = client.describe_instances()

for cl in response['Reservations']:
    for inst in cl['Instances']:
        print(inst)

ec2 = boto3.resource('ec2')


def get_instances():
    for cl in response['Reservations']:
        for inst in cl['Instances']:
            print(inst)

def make_machine():


    ec2.create_instances(InstanceType='t2.micro', ImageId='ami-0fe472d8a85bc7b0e', MinCount=1, MaxCount=1)


def stop_machine():
    for cl in response['Reservations']:
        for inst in cl['Instances']:
            print(inst['InstanceId'])
            vary = inst['InstanceId']
            print(f'ec2.instances.filter(InstanceIds=[{vary}])')
            ec2.instances.filter(InstanceIds=[vary]).terminate()
    #aws ec2 stop-instances --instance-ids i-1234567890abcdef0
    #v#'ec2.stop-instances --instance-ids' + inst['InstanceId']


stop_machine()