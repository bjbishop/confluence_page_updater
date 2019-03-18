#!/usr/bin/env python3
# [[file:~/tsk/confluence_page_updater/readme.txt::add_label][add_label]]
# Add a label to a page
import requests
import json
import getpass
import subprocess

url = "https://confluence.assessment.pearson.com/rest/api/content/19742133/label"
username = getpass.getuser()
password = subprocess.getstatusoutput('security -q find-generic-password -l epic -w')[1]
auth = (username, password)

headers = { "content-type": "application/json" }

data = [
    {
	"prefix": "global",
	"name": "TESTING3"
    }
]

data_json = json.dumps(data)

response = requests.post(
    url,
    auth=auth,
    data=data_json,
    headers = headers,
)

response.raise_for_status()
print(response.json())
# add_label ends here
