cd C:\Users\murug\Documents\ssh_key_files
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-54-66-159-110.ap-southeast-2.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set servername "Indexer" -auth admin:Pa55word'
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-54-66-159-110.ap-southeast-2.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set default-hostname "Indexer" -auth admin:Pa55word'
curl -X POST -k -u admin:Pa55word https://54.66.159.110:8089/servicesNS/nobody/system/data/ui/global-banner/BANNER_MESSAGE_SINGLETON -d global_banner.message="Indexer" -d global_banner.background_color="blue" -d global_banner.visible=true
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-54-66-159-110.ap-southeast-2.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'

ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-13-211-176-199.ap-southeast-2.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set servername "Search_Head" -auth admin:Pa55word'
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-13-211-176-199.ap-southeast-2.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set default-hostname "Search_Head" -auth admin:Pa55word'
curl -X POST -k -u admin:Pa55word https://13.211.176.199:8089/servicesNS/nobody/system/data/ui/global-banner/BANNER_MESSAGE_SINGLETON -d global_banner.message="Search_Head" -d global_banner.background_color="yellow" -d global_banner.visible=true
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-13-211-176-199.ap-southeast-2.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'

ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-3-25-84-151.ap-southeast-2.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set servername "Forwarder" -auth admin:Pa55word'
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-3-25-84-151.ap-southeast-2.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set default-hostname "Forwarder" -auth admin:Pa55word'
curl -X POST -k -u admin:Pa55word https://3.25.84.151:8089/servicesNS/nobody/system/data/ui/global-banner/BANNER_MESSAGE_SINGLETON -d global_banner.message="Forwarder" -d global_banner.background_color="green" -d global_banner.visible=true
ssh -o "StrictHostKeyChecking no" -i sydney_softmania.pem ec2-user@ec2-3-25-84-151.ap-southeast-2.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'