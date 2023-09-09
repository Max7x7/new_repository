import requests
import zipfile
import os
import subprocess
import hashlib

github_url = "https://www.vpnbook.com/free-openvpn-account/vpnbook-openvpn-us2.zip"
local_path = "1.zip"
destination_folder = "zip"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

response = requests.get(github_url)

if response.status_code == 200:
    new_file_hash = hashlib.md5(response.content).hexdigest()
    
    previous_file_hash = ""
    previous_hash_file = "previous_hash.txt"
    if os.path.exists(previous_hash_file):
        with open(previous_hash_file, "r") as hash_file:
            previous_file_hash = hash_file.read()

    if new_file_hash != previous_file_hash:
        with open(local_path, "wb") as file:
            file.write(response.content)

        with zipfile.ZipFile(local_path, "r") as zip_ref:
            zip_ref.extractall(destination_folder)

        with open(previous_hash_file, "w") as hash_file:
            hash_file.write(new_file_hash)

    else:
        print("No new file found. Not downloading or extracting.")
else:
    print("Failed to download the file. Status code: {}".format(response.status_code))
