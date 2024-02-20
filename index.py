import boto3
import json

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

instances = response["Reservations"][0]["Instances"]

for instance in instances:
    for tag in instance["Tags"]:
        if tag["Key"] == "Name":
            print(tag["Value"])
    print("ssh -i {}.pem ec2-user@{}".format(instance["KeyName"],instance["PublicDnsName"]))
    print("""
    """)
