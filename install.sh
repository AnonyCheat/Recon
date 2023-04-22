#!/bin/bash

# Install required packages
sudo apt-get update
sudo apt-get -y install python3 python3-pip masscan nmap eyewitness sublist3r amass assetfinder knockpy zmap

# Install required Python packages
sudo pip3 install requests discord

# Download nessuscli and make it executable
# curl -LJO https://www.tenable.com/downloads/api/v1/public/pages/nessus/downloads/14448/download?i_agree_to_tenable_license_agreement=true
# mv download?i_agree_to_tenable_license_agreement=true Nessus.deb
# sudo dpkg -i Nessus.deb
# sudo /opt/nessus/sbin/nessuscli agent link --key=[ADD YOUR KEY HERE] --groups "example_group" --name "example_agent"
# sudo chmod +x /opt/nessus/sbin/nessuscli

# Download openvas and make it executable
# sudo apt-get -y install software-properties-common
# sudo add-apt-repository -y ppa:mrazavi/openvas
# sudo apt-get update
# sudo apt-get -y install openvas9
# sudo greenbone-nvt-sync
# sudo greenbone-scapdata-sync
# sudo greenbone-certdata-sync

# Download qualys and make it executable
# curl -LJO https://www.qualys.com/downloads/qhost/QualysCloudAgent.sh
# sudo chmod +x QualysCloudAgent.sh
# sudo bash QualysCloudAgent.sh --mode unattended --customer-url=https://qualysapi.qualys.com --agent-auth-token=[ADD YOUR TOKEN HERE] --option=app_activation=1

# Print installation complete message
echo "Installation complete."
