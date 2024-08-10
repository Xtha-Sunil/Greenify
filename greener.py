from github import Github
from datetime import datetime
import os

today_date = datetime.today().strftime("%Y-%m-%d")

api_key = os.environ['api_key']
g = Github(api_key)

username = "Xtha-Sunil"
repo = g.get_repo(f"{username}/Greenify")

for i in range(8):
    file_path = f"{today_date}/file{i}.txt"
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
