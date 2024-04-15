cd C:\Users\murug\Downloads\
ssh -o "StrictHostKeyChecking no" -i osakakey.pem ec2-user@ec2-15-152-48-168.ap-northeast-3.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set servername "Indexer" -auth admin:Pa55word'
ssh -o "StrictHostKeyChecking no" -i osakakey.pem ec2-user@ec2-15-152-48-168.ap-northeast-3.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set default-hostname "Indexer" -auth admin:Pa55word'
curl -X POST -k -u admin:Pa55word https://15.152.48.168:8089/servicesNS/nobody/system/data/ui/global-banner/BANNER_MESSAGE_SINGLETON -d global_banner.message="Indexer" -d global_banner.background_color="blue" -d global_banner.visible=true
ssh -o "StrictHostKeyChecking no" -i osakakey.pem ec2-user@ec2-15-152-48-168.ap-northeast-3.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'

ssh -o "StrictHostKeyChecking no" -i osakakey.pem ec2-user@ec2-13-208-212-247.ap-northeast-3.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set servername "Search_Head" -auth admin:Pa55word'
ssh -o "StrictHostKeyChecking no" -i osakakey.pem ec2-user@ec2-13-208-212-247.ap-northeast-3.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set default-hostname "Search_Head" -auth admin:Pa55word'
curl -X POST -k -u admin:Pa55word https://13.208.212.247:8089/servicesNS/nobody/system/data/ui/global-banner/BANNER_MESSAGE_SINGLETON -d global_banner.message="Search_Head" -d global_banner.background_color="yellow" -d global_banner.visible=true
ssh -o "StrictHostKeyChecking no" -i osakakey.pem ec2-user@ec2-13-208-212-247.ap-northeast-3.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'

ssh -o "StrictHostKeyChecking no" -i osakakey.pem ec2-user@ec2-13-208-172-81.ap-northeast-3.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set servername "Forwarder" -auth admin:Pa55word'
ssh -o "StrictHostKeyChecking no" -i osakakey.pem ec2-user@ec2-13-208-172-81.ap-northeast-3.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk set default-hostname "Forwarder" -auth admin:Pa55word'
curl -X POST -k -u admin:Pa55word https://13.208.172.81:8089/servicesNS/nobody/system/data/ui/global-banner/BANNER_MESSAGE_SINGLETON -d global_banner.message="Forwarder" -d global_banner.background_color="green" -d global_banner.visible=true
ssh -o "StrictHostKeyChecking no" -i osakakey.pem ec2-user@ec2-13-208-172-81.ap-northeast-3.compute.amazonaws.com sudo runuser -l splunk -c '/opt/splunk/bin/splunk restart'