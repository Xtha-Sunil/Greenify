from github import Github
from datetime import datetime
import os

today_date = datetime.today().strftime("%Y-%m-%d")

g = Github(os.getenv('api_key'))

repo = g.get_repo("Xtha-Sunil/Greenify")

for i in range(8,11):
    file_path = f"{today_date}/new{i}.txt"
    file_content = f"file {i + 1}"
    
    try:
        repo.create_file(
            path=file_path,
            message="Creating a new file",
            content=file_content
        )
        print(f"Created file: {file_path}")
    except Exception as e:
        print(f"Failed to create file: {file_path}. Error: {e}")
