from github import Github
import os
import base64

username = "Max7x7"
token = "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"

folder_path = "/home/rompvmrix/zip"

g = Github(token)

repo_name = "new_repository"

repo = g.get_user().get_repo(repo_name)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if not os.path.isfile(file_path):
        continue

    with open(file_path, "rb") as file:
        file_content = file.read()

    file_content_base64 = base64.b64encode(file_content).decode('utf-8')

    file_path_in_repo = filename

    try:
        file_in_repo = repo.get_contents(file_path_in_repo)
    except Exception as e:
        file_in_repo = None

    if file_in_repo:
        current_file_sha = file_in_repo.sha
    else:
        current_file_sha = None

    upload_data = {
        'message': 'Update file',
        'content': file_content_base64,
        'sha': current_file_sha
    }

    upload_url = "https://api.github.com/repos/{}/{}/contents/{}".format(username, repo_name, file_path_in_repo)

    response = repo._requester.requestJsonAndCheck(
        "PUT",
        upload_url,
        input=upload_data,
    )

    if 'content' in response:
        print("File '{}' successfully updated on GitHub.".format(filename))
    else:
        print("Error updating file '{}': {}".format(filename, response))
