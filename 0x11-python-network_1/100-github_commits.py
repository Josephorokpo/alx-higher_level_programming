#!/usr/bin/python3
"""
Module: github_commits

This module retrieves and prints the 10 most recent commits (from the most recent to oldest)
of a specified repository by a specified owner using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Set up the URL for the GitHub API to fetch commits
    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    # Send GET request to the GitHub API
    response = requests.get(url)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Extract and print the 10 most recent commits
        commits = response.json()[:10]  # Limit to the first 10 commits
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    else:
        print("Failed to retrieve commits. Status code:", response.status_code)
