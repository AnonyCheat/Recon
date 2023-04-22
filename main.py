import os
import subprocess
import discord
import requests
import zipfile


# Discord webhook URL
DISCORD_WEBHOOK_URL = "https://discordapp.com/api/webhooks/1097431025237372959/N_9rwxwvCE4aPg0hR2gv18YxJlGDHnYZLJCfQw1yzpkTAIxlPyxYmGCJWOYHAXP-eJ9p"

# Discord message payload
discord_payload = {
    "content": "Enumeration and Scanning results:"
}

# Step 1: Domain and Subdomain Enumeration, save all results into dosubenumerate.txt.
domain_name = input("Enter the domain name to scan: ")
os.system(f"sublist3r -d {domain_name} -o domain_enumeration.txt")
os.system(f"amass enum -d {domain_name} -o domain_enumeration.txt")
os.system(f"subfinder -d {domain_name} -o domain_enumeration.txt")
os.system(f"assetfinder {domain_name} > domain_enumeration.txt")
os.system(f"knockpy {domain_name} -o domain_enumeration.txt")

print("Domain and Subdomain Enumeration completed.")

# Step 2: Take dosubenumerate.txt from above step, then go ahead with Asset Enumeration and Screenshot capture. Save all results in one folder and name it as a assetenumerate, an save all step 2 data in a zip file.
os.system(f"masscan -p1-65535,U:1-65535 {domain_name} | tee asset_enumeration.txt")
os.system(f"nmap -sS -sU -T4 -A -v -Pn -p- -oN asset_enumeration.txt {domain_name}")

# Using EyeWitness to capture screenshots of the identified domains and subdomains
os.system(f"EyeWitness --web --no-prompt -f domain_enumeration.txt --prepend-https -d screenshots")

# Compressing the EyeWitness output as a zip file
with zipfile.ZipFile("eyewitness_screenshots.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk("screenshots"):
        for file in files:
            zipf.write(os.path.join(root, file))

print("Asset Enumeration and Screenshot capture completed.")

# Step 3: TCP and UDP Scanning
os.system(f"masscan -p1-65535,U:1-65535 $(cat asset_enumeration.txt | awk '/^[^#]/ {{print $4}}' | sort -u) | tee tcp_udp_scan.txt")
os.system(f"nmap -sS -sU -T4 -A -v -Pn -p- -oN tcp_udp_scan.txt $(cat asset_enumeration.txt | awk '/^[^#]/ {{print $4}}' | sort -u)")
os.system(f"zmap -p80 -o zmap_scan.txt $(cat asset_enumeration.txt | awk '/^[^#]/ {{print $4}}' | sort -u)")

print("TCP and UDP Scanning completed.")

# Step 4: Vulnerability Scanning
# Skipping the vulnerability scanning for now

# Step 5: Send results to Discord webhook
discord_files = {
    "Domain Enumeration": open("domain_enumeration.txt", "rb"),
    "Asset Enumeration": open("asset_enumeration.txt", "rb"),
    "TCP and UDP Scan": open("tcp_udp_scan.txt", "rb"),
    "Zmap Scan": open("zmap_scan.txt", "rb"),
    "EyeWitness Screenshots": open("eyewitness_screenshots.zip", "rb")
}

discord_payload["files"] = discord_files


discord_payload["files"] = discord_files

response = requests.post(DISCORD_WEBHOOK_URL, files=discord_files, data=discord_payload)
print(response.text)
