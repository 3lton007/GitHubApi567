

"""
Function to capture names of the repository and their commit values!
@eltonaloys
"""

import requests
import json

def repo(u_id):
    """ Collecting names through Github API """
    repo_name_url = requests.get(f"https://api.github.com/users/{u_id}/repos") 
    repo_name = repo_name_url.json() #Converting to a JSON File

    for value in repo_name:
        repos = value.get("name")

        """ Collecting values of commits from Repository API """
        repo_commit_url = requests.get(f"https://api.github.com/repos/{u_id}/{repos}/commits")
        repo_commit = repo_commit_url.json()      #Converting to a JSON FIle

        com = 0

        for item in repo_commit:
            if item in repo_commit: 

                com = com + 1   #counting number of commits
        
        yield f"Repo: {repos}, Commits: {com}"

def main():
    yolo = input("Enter your user ID:")

    for item in repo(yolo):
        return item

