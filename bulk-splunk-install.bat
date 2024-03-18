cd C:\Users\murug\Documents\ssh_key_files
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-54-66-159-110.ap-southeast-2.compute.amazonaws.com sudo yum install git -y
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-54-66-159-110.ap-southeast-2.compute.amazonaws.com git clone https://github.com/SoftManiaTech/splunk_cluster_admin_training.git
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-54-66-159-110.ap-southeast-2.compute.amazonaws.com sudo chmod +x splunk_cluster_admin_training/splunk-install.sh
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-54-66-159-110.ap-southeast-2.compute.amazonaws.com sudo ./splunk_cluster_admin_training/splunk-install.sh
echo Indexer - Splunk installation is done
echo ======
echo 
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-13-211-176-199.ap-southeast-2.compute.amazonaws.com sudo yum install git -y
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-13-211-176-199.ap-southeast-2.compute.amazonaws.com git clone https://github.com/SoftManiaTech/splunk_cluster_admin_training.git
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-13-211-176-199.ap-southeast-2.compute.amazonaws.com sudo chmod +x splunk_cluster_admin_training/splunk-install.sh
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-13-211-176-199.ap-southeast-2.compute.amazonaws.com sudo ./splunk_cluster_admin_training/splunk-install.sh
echo Search_Head - Splunk installation is done
echo ======
echo 
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-3-25-84-151.ap-southeast-2.compute.amazonaws.com sudo yum install git -y
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-3-25-84-151.ap-southeast-2.compute.amazonaws.com git clone https://github.com/SoftManiaTech/splunk_cluster_admin_training.git
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-3-25-84-151.ap-southeast-2.compute.amazonaws.com sudo chmod +x splunk_cluster_admin_training/splunk-install.sh
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-3-25-84-151.ap-southeast-2.compute.amazonaws.com sudo ./splunk_cluster_admin_training/splunk-install.sh
echo Forwarder - Splunk installation is done
echo ======
echo 
