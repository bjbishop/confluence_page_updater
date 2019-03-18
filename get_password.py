#!/usr/bin/env python3
# [[file:~/tsk/confluence_page_updater/readme.txt::fetch_password][fetch_password]]
import subprocess
a = subprocess.getstatusoutput('security -q find-generic-password -l epic -w')[1]
print(a)
# fetch_password ends here
