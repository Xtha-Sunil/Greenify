from github import Github
from datetime import datetime
import os

# Get today's date and current time for the folder
now = datetime.now()
date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

# GitHub API key from environment variable
api_key = os.environ['api_key']
g = Github(api_key)

username = "Xtha-Sunil"
repo = g.get_repo(f"{username}/Greenify")

# Create files in a single folder using the combined date and time
for i in range(131):
    file_path = f"{date_time}/file{i}.txt"
    file_content = "Automation is helpful."
    
    try:
        repo.create_file(
            path=file_path,
            message="Creating a new file",
            content=file_content
        )
        print(f"Created file: {file_path}")
    except Exception as e:
        print(f"Failed to create file: {file_path}. Error: {e}")
