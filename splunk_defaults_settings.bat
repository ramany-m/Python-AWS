cd C:\Users\muham\Downloads\
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com runuser -l splunk -c '/opt/splunk/bin/splunk set servername "Indexer"'
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com runuser -l splunk -c '/opt/splunk/bin/splunk set default-hostname "Indexer"'
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com echo [BANNER_MESSAGE_SINGLETON] >> /opt/splunk/etc/system/local/global-banner.conf
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com echo global_banner.visible = true >> /opt/splunk/etc/system/local/global-banner.conf
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com echo global_banner.message = Indexer >> /opt/splunk/etc/system/local/global-banner.conf
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com echo global_banner.background_color = blue >> /opt/splunk/etc/system/local/global-banner.conf
ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-15-237-121-173.eu-west-3.compute.amazonaws.com runuser -l splunk -c '/opt/splunk/bin/splunk restart'


@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com runuser -l splunk -c '/opt/splunk/bin/splunk set servername "Search_Head"'
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com runuser -l splunk -c '/opt/splunk/bin/splunk set default-hostname "Search_Head"'
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com echo [BANNER_MESSAGE_SINGLETON] > /opt/splunk/etc/system/local/global-banner.conf
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com echo global_banner.visible = true > /opt/splunk/etc/system/local/global-banner.conf
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com echo global_banner.message = Search_Head > /opt/splunk/etc/system/local/global-banner.conf
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com echo global_banner.background_color = yellow > /opt/splunk/etc/system/local/global-banner.conf
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-13-38-97-216.eu-west-3.compute.amazonaws.com runuser -l splunk -c '/opt/splunk/bin/splunk restart'

@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com runuser -l splunk -c '/opt/splunk/bin/splunk set servername "Forwarder"'
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com runuser -l splunk -c '/opt/splunk/bin/splunk set default-hostname "Forwarder"'
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com echo [BANNER_MESSAGE_SINGLETON] > /opt/splunk/etc/system/local/global-banner.conf
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com echo global_banner.visible = true > /opt/splunk/etc/system/local/global-banner.conf
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com echo global_banner.message = Forwarder > /opt/splunk/etc/system/local/global-banner.conf
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com echo global_banner.background_color = green > /opt/splunk/etc/system/local/global-banner.conf
@REM ssh -o "StrictHostKeyChecking no" -i pariskey.pem.pem ec2-user@ec2-35-181-4-180.eu-west-3.compute.amazonaws.com runuser -l splunk -c '/opt/splunk/bin/splunk restart'