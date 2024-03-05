cd C:\Users\muham\Downloads\
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com sudo yum install git -y
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com git clone https://github.com/SoftManiaTech/splunk_cluster_admin_training.git
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com sudo chmod +x splunk_cluster_admin_training/splunk-install.sh
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com sudo ./splunk_cluster_admin_training/splunk-install.sh
echo Indexer - Splunk installation is done
echo ======
echo 
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com sudo yum install git -y
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com git clone https://github.com/SoftManiaTech/splunk_cluster_admin_training.git
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com sudo chmod +x splunk_cluster_admin_training/splunk-install.sh
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com sudo ./splunk_cluster_admin_training/splunk-install.sh
echo Search_Head - Splunk installation is done
echo ======
echo 
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com sudo yum install git -y
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com git clone https://github.com/SoftManiaTech/splunk_cluster_admin_training.git
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com sudo chmod +x splunk_cluster_admin_training/splunk-install.sh
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com sudo ./splunk_cluster_admin_training/splunk-install.sh
echo Forwarder - Splunk installation is done
echo ======
echo 
