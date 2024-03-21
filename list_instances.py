import boto3
ec2 = boto3.client('ec2')
ec2list=[]
regions = ec2.describe_regions().get('Regions',[] )
#print("Region",regions)

    # Iterate over regions
for region in regions:

        #print ("* Checking region  --   %s " % region['RegionName'])
        reg=region['RegionName']

        client = boto3.client('ec2', region_name=reg)
        response = client.describe_instances()

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                #print ("  ---- Instance %s in %s" % (instance['InstanceId'], region['RegionName']))
                ec2list.append(instance['InstanceId'])

print(ec2list)

#for instance in ec2list:
#     response = client.describe_instances()

#print(response)
     
