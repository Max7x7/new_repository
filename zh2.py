import os
import requests
import base64
import json

access_token = "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"
repository_name = "new_repository"
folder_path = "/home/rompvmrix/zip"
username = "Max7x7"

headers = {
    'Authorization': 'token ' + access_token,
    'Content-Type': 'application/json',
}

for filename in os.listdir(folder_path):
    if "2500" in filename:
        file_path_in_repo = filename
        with open(os.path.join(folder_path, filename), 'rb') as file:
            file_content = file.read()
        file_content_base64 = base64.b64encode(file_content)

        get_file_url = "https://api.github.com/repos/{}/{}/contents/{}".format(username, repository_name, file_path_in_repo)
        response = requests.get(get_file_url, headers=headers)

        if response.status_code == 200:
            current_file_sha = response.json().get('sha')
        else:
            print("Error getting current file information for {}: {}".format(filename, response.status_code))
            print(response.text)
            current_file_sha = None

        data = {
            'message': 'Update file',
            'content': file_content_base64.decode('utf-8'),
            'sha': current_file_sha
        }

        upload_url = "https://api.github.com/repos/{}/{}/contents/{}".format(username, repository_name, file_path_in_repo)

        response = requests.put(upload_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            print("File {} successfully updated on GitHub.".format(filename))
        else:
            print("Error updating file {}: {}".format(filename, response.status_code))
            print(response.text)
