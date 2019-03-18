# -*- mode: org -*-

* Adding a label

#+NAME: add_label
#+HEADER:
#+BEGIN_SRC python :tangle add_label.py :shebang #!/usr/bin/env python3 :comments link :results output
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
  #+END_SRC

  #+RESULTS: add_label
  : {'results': [{'prefix': 'global', 'name': 'aws', 'id': '3801168'}, {'prefix': 'global', 'name': 'security', 'id': '14123188'}, {'prefix': 'global', 'name': 'key', 'id': '6783758'}, {'prefix': 'global', 'name': 'rotation', 'id': '16089753'}, {'prefix': 'global', 'name': 'rotate', 'id': '16089883'}, {'prefix': 'global', 'name': 'testing3', 'id': '16089892'}], 'start': 0, 'limit': 200, 'size': 6}

* Deleting a label
#+NAME: delete_label
#+HEADER:
#+BEGIN_SRC python :tangle del_label.py :shebang #!/usr/bin/env python3 :comments link :results output
  # Add a label to a page
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
#+END_SRC

#+RESULTS: delete_label
: <Response [204]>
* Fetching the password
#+NAME: fetch_password
#+HEADER:
#+BEGIN_SRC python :tangle get_password.py :shebang #!/usr/bin/env python3 :results output :comments link
  import subprocess
  a = subprocess.getstatusoutput('security -q find-generic-password -l epic -w')[1]
  print(a)
#+END_SRC
