import boto3
import json
from botocore.config import Config
import pprint
import os
import subprocess
import yaml

with open('defaults.yml', 'r') as file:
    defaults=yaml.safe_load(file)

script_file_name = "bulk-splunk-install.bat"
monitoring_console_connection_commands_file_name = "monitoring_console_connection_commands.bat"


pp = pprint.PrettyPrinter(indent=1)

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
    if os.path.isfile(script_file_name):
        os.remove(script_file_name)
    with open(script_file_name, "a+") as file:
        file.write("cd {}".format(defaults["pem_file_path"]))
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
    with open('instance_details.yml', 'r') as file:
        instance_details=yaml.safe_load(file)
    pem_file_name = instance_details["Cluster_Manager"]["ssh_key"]
    YOUR_CLUSTER_MANAGER_PRIVATE_IP = instance_details["Cluster_Manager"]["private_ip"]
    YOUR_CLUSTER_MANAGER_PUBLIC_IP = instance_details["Cluster_Manager"]["public_ip"]
    YOUR_INDEXER_1_PRIVATE_IP = instance_details["Indexer_1"]["private_ip"]
    YOUR_INDEXER_1_PUBLIC_IP = instance_details["Indexer_1"]["public_ip"]
    YOUR_INDEXER_2_PRIVATE_IP = instance_details["Indexer_2"]["private_ip"]
    YOUR_INDEXER_2_PUBLIC_IP = instance_details["Indexer_2"]["public_ip"]
    YOUR_INDEXER_3_PRIVATE_IP = instance_details["Indexer_3"]["private_ip"]
    YOUR_INDEXER_3_PUBLIC_IP = instance_details["Indexer_3"]["private_ip"]
    YOUR_SH_1_PRIVATE_IP = instance_details["Search_Head_1"]["private_ip"]
    YOUR_SH_1_PUBLIC_IP = instance_details["Search_Head_1"]["public_ip"]
    YOUR_SH_2_PRIVATE_IP = instance_details["Search_Head_2"]["private_ip"]
    YOUR_SH_2_PUBLIC_IP = instance_details["Search_Head_2"]["public_ip"]
    YOUR_SH_3_PRIVATE_IP = instance_details["Search_Head_3"]["private_ip"]
    YOUR_SH_3_PUBLIC_IP = instance_details["Search_Head_3"]["public_ip"]
    YOUR_DEPLOYER_PRIVATE_IP = instance_details["Deployer"]["private_ip"]
    YOUR_DEPLOYER_PUBLIC_IP = instance_details["Deployer"]["public_ip"]
    ssh_command_prefix = 'ssh -o "StrictHostKeyChecking no" -i {}.pem ec2-user@'.format(pem_file_name)
    
    with open("splunk_infra_config.bat", "a+") as file:
        file.write("cd {}".format(defaults["pem_file_path"]))
        file.write("\n")
        #Cluster Manager:
        file.write("echo ====== Cluster Manager =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_CLUSTER_MANAGER_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk edit cluster-config -mode manager -replication_factor 3 -search_factor 2 -secret IndexerClusterKey123 -cluster_label softmania_cluster1 -auth admin:Pa55word'")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_CLUSTER_MANAGER_PUBLIC_IP + " sudo runuser -l splunk -c 'echo -e \"[indexer_discovery]\\npass4SymmKey = IndexerDiscoveryKey123\\npolling_rate = 10\\nindexerWeightByDiskCapacity = true\" >> /opt/splunk/etc/system/local/server.conf'")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_CLUSTER_MANAGER_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'")
        file.write("\n")

        #Indexer 1:
        file.write("echo ====== Indexer 1 =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_INDEXER_1_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk edit cluster-config -mode peer -manager_uri https://{}:8089 -replication_port 9887 -secret IndexerClusterKey123 -auth admin:Pa55word'".format(YOUR_CLUSTER_MANAGER_PRIVATE_IP))
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_INDEXER_1_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'")
        file.write("\n")

        #Indexer 2:
        file.write("echo ====== Indexer 2 =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_INDEXER_2_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk edit cluster-config -mode peer -manager_uri https://{}:8089 -replication_port 9887 -secret IndexerClusterKey123 -auth admin:Pa55word'".format(YOUR_CLUSTER_MANAGER_PRIVATE_IP))
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_INDEXER_2_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'")
        file.write("\n")
        
        #Indexer 3:
        file.write("echo ====== Indexer 3 =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_INDEXER_3_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk edit cluster-config -mode peer -manager_uri https://{}:8089 -replication_port 9887 -secret IndexerClusterKey123 -auth admin:Pa55word'".format(YOUR_CLUSTER_MANAGER_PRIVATE_IP))
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_INDEXER_3_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'")
        file.write("\n")

        #Deployer:
        file.write("echo ====== Deployer =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_DEPLOYER_PUBLIC_IP + " sudo runuser -l splunk -c 'echo -e \"[shclustering]\\npass4SymmKey = SoftManiaSHClusterKey\\nshcluster_label = shcluster1\" >> /opt/splunk/etc/system/local/server.conf'")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_DEPLOYER_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'")
        file.write("\n")


        #Search Head 1: 
        file.write("echo ====== Search Head 1 =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_1_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk init shcluster-config -auth admin:Pa55word -mgmt_uri https://{}:8089 -replication_port 9000 -replication_factor 3 -conf_deploy_fetch_url https://{}:8089 -secret SoftManiaSHClusterKey -shcluster_label softmania_shcluster1'".format(YOUR_SH_1_PRIVATE_IP,YOUR_DEPLOYER_PRIVATE_IP))
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_1_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'")
        file.write("\n")

        #Search Head 2: 
        file.write("echo ====== Search Head 2 =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_2_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk init shcluster-config -auth admin:Pa55word -mgmt_uri https://{}:8089 -replication_port 9000 -replication_factor 3 -conf_deploy_fetch_url https://{}:8089 -secret SoftManiaSHClusterKey -shcluster_label softmania_shcluster1'".format(YOUR_SH_2_PRIVATE_IP,YOUR_DEPLOYER_PRIVATE_IP))
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_2_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'")
        file.write("\n")

        #Search Head 3: 
        file.write("echo ====== Search Head 3 =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_3_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk init shcluster-config -auth admin:Pa55word -mgmt_uri https://{}:8089 -replication_port 9000 -replication_factor 3 -conf_deploy_fetch_url https://{}:8089 -secret SoftManiaSHClusterKey -shcluster_label softmania_shcluster1'".format(YOUR_SH_3_PRIVATE_IP,YOUR_DEPLOYER_PRIVATE_IP))
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_3_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'")
        file.write("\n")

        #Search Head 1: 
        file.write("echo ====== Search Head 1 =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_1_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk bootstrap shcluster-captain -servers_list \"https://{}:8089,https://{}:8089,https://{}:8089\" -auth admin:Pa55word'".format(YOUR_SH_1_PRIVATE_IP,YOUR_SH_2_PRIVATE_IP,YOUR_SH_3_PRIVATE_IP))
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_1_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk edit cluster-config -mode searchhead -manager_uri https://{}:8089 -secret IndexerClusterKey123 -auth admin:Pa55word'".format(YOUR_CLUSTER_MANAGER_PRIVATE_IP))
        file.write("\n")

        #Search Head 2:
        file.write("echo ====== Search Head 2 =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_2_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk edit cluster-config -mode searchhead -manager_uri https://{}:8089 -secret IndexerClusterKey123 -auth admin:Pa55word'".format(YOUR_CLUSTER_MANAGER_PRIVATE_IP))
        file.write("\n")

        #Search Head 3:
        file.write("echo ====== Search Head 2 =====")
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_3_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk edit cluster-config -mode searchhead -manager_uri https://{}:8089 -secret IndexerClusterKey123 -auth admin:Pa55word'".format(YOUR_CLUSTER_MANAGER_PRIVATE_IP))
        file.write("\n")
        file.write(ssh_command_prefix + YOUR_SH_3_PUBLIC_IP + " sudo runuser -l splunk -c '/opt/splunk/bin/splunk rolling-restart shcluster-members'")
        file.write("\n")

def monitoring_console_connection():
    monitoring_console_server = ""

    with open('instance_details.yml', 'r') as file:
        instance_details=yaml.safe_load(file)
        
    monitoring_console_server = instance_details["Monitoring_Console"]["public_ip"]

    for instance in instance_list:
        with open(monitoring_console_connection_commands_file_name, "a+") as file:
                file.write("curl -k -u {}:{} https://{}:8089/services/authentication/users -d name={} -d password={} -d roles=admin".format(defaults["splunk_admin_user"], defaults["splunk_admin_password"],instance["PublicIpAddress"],defaults["splunk_service_user"],defaults["splunk_service_password"]))
                file.write("\n")
                file.write("curl -k -u {}:{} https://{}:8089/services/search/distributed/peers -d name={}:8089 -d remoteUsername={} -d remotePassword={}".format(defaults["splunk_admin_user"], defaults["splunk_admin_password"],monitoring_console_server,instance["PrivateIpAddress"],defaults["splunk_service_user"],defaults["splunk_service_password"]))
                file.write("\n")

# start_instance()
# stop_instance()
# get_ssh_commands()
# prepare_splunk_installation()
# execute_batch_script()
# monitoring_console_connection()
configure_the_infrastructure()