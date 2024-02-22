import boto3
import json
from botocore.config import Config
import pprint

pp = pprint.PrettyPrinter(indent=1)

my_config = Config(
    region_name = 'ap-southeast-2'
)

ec2 = boto3.client('ec2', config=my_config)
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-type',
            'Values': [
                't2.medium',
            ],
        },
    ]
)

# pp.pprint(response)

# with open("test.json","a+") as filejson:
#     filejson.write(str(response))

instance_list = []

for instances_array in response["Reservations"]:
    for instance in instances_array["Instances"]:
        instance_list.append(instance)

command_array = []
with open("userdata.txt") as file:
    for command in file.readlines():
        command_array.append(command.strip())
# print(array)

instance_array = []


for instance in instance_list:
    instance_array.append(instance["InstanceId"])

# print(instance_array)

def start_instance():
    response = ec2.start_instances(
        InstanceIds=instance_array
    )
    print(response)

def stop_instance():
    response = ec2.stop_instances(
        InstanceIds=instance_array
    )
    print(response)


def get_ssh_commands():
    for instance in instance_list:
        for tag in instance["Tags"]:
            if tag["Key"] == "Name":
                print(tag["Value"])
        print("ssh -i {}.pem ec2-user@{}".format(instance["KeyName"],instance["PublicDnsName"]))
        print("""
        """)


def prepare_splunk_installation():
    with open("bulk-splunk-install.bat", "a+") as file:
        file.write("cd C:\\Users\\raman\\Downloads\\")
        file.write("\n")
    for instance in instance_list:
        ssh_command = 'ssh -o "StrictHostKeyChecking no" -i {}.pem ec2-user@{}'.format(instance["KeyName"],instance["PublicDnsName"])
        for command in command_array:
            print(ssh_command, command)
            with open("bulk-splunk-install.bat", "a+") as file:
                file.write(ssh_command+" "+command)
                file.write("\n")
        
        instance_name = ""
        for tag in instance["Tags"]:
            if tag["Key"] == "Name":
                # print(tag["Value"])
                instance_name=tag["Value"]
        print("echo {} - Splunk installation is done".format(instance_name))
        with open("bulk-splunk-install.bat", "a+") as file:
                file.write("echo {} - Splunk installation is done".format(instance_name))
                file.write("\n")
                file.write("echo ======")
                file.write("\n")
                file.write("echo ")
                file.write("\n")



# start_instance()
prepare_splunk_installation()
# stop_instance()
# get_ssh_commands()
