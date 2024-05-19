import boto3
import json
from botocore.config import Config
import pprint
import os
import subprocess
import yaml

with open('defaults.yml', 'r') as file:
    defaults=yaml.safe_load(file)


my_config = Config(
    region_name = defaults["region_name"]
)

ec2 = boto3.client('ec2', config=my_config)
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-type',
            'Values': [
                defaults["instance_configs"]["type"],
            ],
        },
    ]
)

instance_list = []

for instances_array in response["Reservations"]:
    for instance in instances_array["Instances"]:
        instance_list.append(instance)

instance_details_yml={}
for count, instance in enumerate(instance_list):
    
    print(count, instance["PrivateIpAddress"])
    instance_name = defaults["instance_configs"]["names"][count]
    # response = ec2.create_tags(
    #     Resources=[
    #         instance["InstanceId"],
    #     ],
    #     Tags=[
    #         {
    #             'Key': 'Name',
    #             'Value': instance_name,
    #         },
    #     ],
    # )
    instance_details_yml[instance_name]={"private_ip":instance["PrivateIpAddress"],"public_ip":instance["PublicIpAddress"], "ssh_key":instance["KeyName"]}

if os.path.isfile("instance_details.yml"):
    os.remove("instance_details.yml")

with open("instance_details.yml", "a+") as yml_file:
    yaml.dump(instance_details_yml, yml_file)
    
    # print(response)
