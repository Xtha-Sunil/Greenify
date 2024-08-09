from github import Github
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Get today's date
today_date = datetime.today().strftime("%Y-%m-%d")

# Fetch the API key from environment variables
api_key = os.getenv('api_key')
if not api_key:
    raise ValueError("API key not found. Ensure it's set in the environment variables.")

# Authenticate with GitHub
g = Github(api_key)

# Access the repository
repo = g.get_repo("Xtha-Sunil/Greenify")

# Create files in the repository
for i in range(1, 7):
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
