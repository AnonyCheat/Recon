Domain Enumeration and Vulnerability Scanning Tool

This tool is designed to help with the process of domain enumeration and vulnerability scanning for a given domain. It uses several open-source tools and frameworks to perform the following tasks:

Domain and subdomain enumeration
Asset enumeration and screenshot capture
TCP and UDP scanning
Vulnerability scanning

Usage

Install the required tools by running the install_tools.sh script.

Run the main Python script main.py and enter the domain name you want to scan when prompted.

The tool will then perform domain enumeration using Sublist3r, Amass, Subfinder, Assetfinder, and Knockpy. The results will be saved in domain_enumeration.txt.

The tool will then perform asset enumeration and screenshot capture using Masscan, Nmap, and EyeWitness. The results will be saved in the asset_enumeration folder, and a zip file containing all the results will be created.

The tool will then perform TCP and UDP scanning using Masscan, Nmap, and Zmap. The results will be saved in tcp_udp_scan.txt and zmap_scan.txt.

The tool will then perform vulnerability scanning using Nessus, OpenVAS, and Qualys. The results will be saved in their respective output files.

All the results will be sent to the Discord webhook specified in discord_payload along with the domain name.

Requirements

Python 3
Sublist3r
Amass
Subfinder
Assetfinder
Knockpy
Masscan
Nmap
EyeWitness
Nessus
OpenVAS
Qualys

Credits
This tool was created by Chetan Tiwari and is based on several open-source tools and frameworks.

Sublist3r
Amass
Subfinder
Assetfinder
Knockpy
Masscan
Nmap
EyeWitness
Nessus
OpenVAS
Qualys

