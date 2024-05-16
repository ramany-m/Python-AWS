import boto3
import json
from botocore.config import Config
import pprint
import os
import subprocess

script_file_name = "bulk-splunk-install.bat"

if os.path.isfile(script_file_name):
    os.remove(script_file_name)

pp = pprint.PrettyPrinter(indent=1)

my_config = Config(
    region_name = 'ap-northeast-1'
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

def instance_banner_color(instance_name):
    if "Indexer" in instance_name:
        return "blue"
    elif "SH" in instance_name:
        return "green"
    elif "Deploy" in instance_name:
        return "yellow"
    elif "License" in instance_name:
        return "orange"
    else:
        return "red"

def prepare_splunk_installation():
    with open(script_file_name, "a+") as file:
        file.write("cd C:\\Users\\murug\\Downloads\\")
        file.write("\n")
    for instance in instance_list:
        # print(instance)
        # break
        ssh_command = 'ssh -o "StrictHostKeyChecking no" -i {}.pem ec2-user@{}'.format(instance["KeyName"],instance["PublicDnsName"])
        for command in command_array:
            print(ssh_command, command)
            with open(script_file_name, "a+") as file:
                file.write(ssh_command+" "+command)
                file.write("\n")
        instance_name = ""
        for tag in instance["Tags"]:
            if tag["Key"] == "Name":
                # print(tag["Value"])
                instance_name=tag["Value"]

        with open(script_file_name, "a+") as file:
                file.write(ssh_command+" "+"sudo runuser -l splunk -c '/opt/splunk/bin/splunk set servername \"{}\" -auth admin:Pa55word'".format(instance_name))
                file.write("\n")
                file.write(ssh_command+" "+"sudo runuser -l splunk -c '/opt/splunk/bin/splunk set default-hostname \"{}\" -auth admin:Pa55word'".format(instance_name))
                file.write("\n")
                file.write('curl -X POST -k -u admin:Pa55word https://{}:8089/servicesNS/nobody/system/data/ui/global-banner/BANNER_MESSAGE_SINGLETON -d global_banner.message="{}" -d global_banner.background_color="{}" -d global_banner.visible=true'.format(instance["PublicIpAddress"],instance_name, instance_banner_color(instance_name)))
                file.write("\n")
                file.write(ssh_command+" "+"sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'")
                file.write("\n")


        print("echo {} - Splunk installation is done".format(instance_name))
        with open(script_file_name, "a+") as file:
                file.write("echo {} - Splunk installation is done".format(instance_name))
                file.write("\n")
                file.write("echo ======")
                file.write("\n")
                file.write("echo ")
                file.write("\n")

def execute_batch_script():
    print("Executing Batch script --> bulk-splunk-install.bat")
    subprocess.run([r"bulk-splunk-install.bat"])

def configure_the_infrastructure():
    pass

# start_instance()
# stop_instance()
# get_ssh_commands()
prepare_splunk_installation()
execute_batch_script()
