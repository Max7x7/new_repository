import requests
import zipfile
import os
import subprocess

github_url = "https://www.vpnbook.com/free-openvpn-account/vpnbook-openvpn-pl226.zip"
local_path = "1.zip"
destination_folder = "zip"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

response = requests.get(github_url)

if response.status_code == 200:
    with open(local_path, "wb") as file:
        file.write(response.content)

    with zipfile.ZipFile(local_path, "r") as zip_ref:
        zip_ref.extractall(destination_folder)

    print("File downloaded and saved as {}".format(local_path))
    print("Contents extracted to {}".format(destination_folder))

    print("File successfully downloaded and extracted.")
    
    subprocess.call(["python", "zh2.py"])
else:
    print("Failed to download the file. Status code: {}".format(response.status_code))
