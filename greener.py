from github import Github
from datetime import datetime
import os

today_date = datetime.today().strftime("%Y-%m-%d")

api_key = os.environ['api_key']
g = Github(api_key)

repo = g.get_repo("Xtha-Sunil/Greenify")

for i in range(1,7):
    repo.create_file(
        path=f"{today_date}/new{i}.txt",
        message="Creating a new file",
        content=f"file {i + 1}"
    )
