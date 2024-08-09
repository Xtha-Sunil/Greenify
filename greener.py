from github import Github
from datetime import datetime
import os

# Get today's date in the format YYYY-MM-DD
today_date = datetime.today().strftime("%Y-%m-%d")

# Authenticate with GitHub using the API key stored in environment variables
g = Github(os.getenv('API_KEY'))

# Retrieve the authenticated user's username
user = g.get_user()
username = user.login

# Get the repository object for the user's 'Greenify' repository
repo = g.get_repo(f"{username}/Greenify")

# Loop to create 8 new files in the repository
for i in range(8):
    # Define the file path and content
    file_path = f"{today_date}/new{i}.txt"
    file_content = f"file {i + 1}"
    
    try:
        # Attempt to create a new file in the repository
        repo.create_file(
            path=file_path,
            message="Creating a new file",
            content=file_content
        )
        print(f"Created file: {file_path}")
    except Exception as e:
        # Handle any errors that occur during file creation
        print(f"Failed to create file: {file_path}. Error: {e}")
