# Automated Daily Commits for a Green GitHub Heatmap

This automation will make daily commits to ensure your GitHub heatmap stays green. Follow the steps below to set it up:

1. **Fork the Repository**: Start by forking this repository to your GitHub account.

2. **Create a Fine-Grained Token**:
   - Go to your GitHub settings and create a fine-grained personal access token with `Contents` permission set to `read and write`.

3. **Add the API Key to Repository Secrets**:
   - Navigate to the repository settings in your forked repo.
   - Add the API key as a repository secret with the name `API_KEY`.

4. **Modify the `greener.py` Script**:
   - The script currently encounters a `401 Unauthorized` error when running in GitHub Actions due to the API key not being associated with the correct username.
   - To fix this, update line 10 of `greener.py` to:
     ```python
     username = "your_github_username"
     ```
   - Replace `"your_github_username"` with your actual GitHub username.

5. **Enable the Workflow**:
   - Go to the `Actions` tab in your repository and enable the workflow.

Once set up, the workflow will run daily, making a commit to keep your GitHub heatmap green.
