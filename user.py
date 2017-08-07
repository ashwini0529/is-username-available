#!/usr/bin/python
import sys
import requests
"""
Usage: python user.py 
Platforms covered:
1. Github
2. Gitlab
3. Bitbucket
4. OpenHub
5. OpenSuse
"""
GITHUB_BASE_URL="https://github.com/"
GITLAB_BASE_URL="https://gitlab.com/api/v4/users?username="
BITBUCKET_BASE_URL="https://api.bitbucket.org/2.0/users/"
OPENHUB_BASE_URL="https://www.openhub.net/accounts/"
OPENSUSE_BASE_URL="https://connect.opensuse.org/pg/profile/"
usernameStatusContainer=[]
arguments = sys.argv
username = arguments[1]
def isUsernameValid(username):
	#Github
	r=requests.get(GITHUB_BASE_URL+username)
	statusCode = r.status_code
	isGithubUsernameTaken=0
	if(statusCode==200):
		isGithubUsernameTaken=1
	usernameStatusContainer.append(
		generateDictionary(GITHUB_BASE_URL,"GitHub",isGithubUsernameTaken)
		)
	#Gitlab
	r=requests.get(GITLAB_BASE_URL+username)
	isGitlabUsernameTaken=len(r.json())
	usernameStatusContainer.append(
		generateDictionary(GITLAB_BASE_URL,"GitLab",isGitlabUsernameTaken)
		)
	#Bitbucket
	r=requests.get(BITBUCKET_BASE_URL+username)
	data=r.json()
	isBitbucketUsernameTaken=0
	if(data["type"]=="error" and data["error"]["message"]==username):
		pass
	else:
		isBitbucketUsernameTaken=1
	usernameStatusContainer.append(
		generateDictionary(BITBUCKET_BASE_URL,"BitBucket",isBitbucketUsernameTaken)
		)
	#OpenHub
	r=requests.get(OPENHUB_BASE_URL+username)
	isOpenHubUsernameTaken=0
	if(r.status_code==200):
		isOpenHubUsernameTaken=1
	usernameStatusContainer.append(
		generateDictionary(OPENHUB_BASE_URL,"OpenHub",isOpenHubUsernameTaken)
		)
	#OpenSuse
	r=requests.get(OPENSUSE_BASE_URL+username)
	isOpenSuseUsernameAvailable=1
	if("Sorry" in r.text):
		isOpenSuseUsernameAvailable=0
	usernameStatusContainer.append(
		generateDictionary(OPENSUSE_BASE_URL,"OpenSUSE",isOpenSuseUsernameAvailable)
		)
	return usernameStatusContainer
"""
Function to generate Service Dictionary
"""
def generateDictionary(url,service,status):
	serviceDictionary={
	"service":service,
	"url":url,
	"status":status
	}
	return serviceDictionary

print(isUsernameValid(username))