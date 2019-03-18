#!/usr/bin/env python3
# [[file:~/tsk/confluence_page_updater/readme.txt::delete_label][delete_label]]
# Remove a label from a page
import requests
import getpass
import subprocess

url = "https://confluence.assessment.pearson.com/rest/api/content/19742133/label/testing3"
username = getpass.getuser()
password = subprocess.getstatusoutput('security -q find-generic-password -l epic -w')[1]
auth = (username, password)

response = requests.delete(
    url,
    auth=auth,
)

response.raise_for_status()
print(response)
# delete_label ends here
