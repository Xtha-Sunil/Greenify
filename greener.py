name: Manual Trigger Job

on:
  workflow_dispatch:

jobs:
  run-script:
    runs-on: ubuntu-latest

    env:
      API_KEY: ${{ secrets.API_KEY }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x' # Specify the Python version you want

      - name: Debug - Print Environment Variable
        run: echo "API_KEY is set"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install PyGithub

      - name: Run script
        run: |
          python greener.py
