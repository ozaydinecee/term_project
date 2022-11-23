import requests
from requests.auth import HTTPBasicAuth

url = "https://termproject.atlassian.net/rest/api/3/issue/PROJ-5"

auth = HTTPBasicAuth("ozaydine@mef.edu.tr", "Wjs8qOB4SKSoZyDp0dax400A")

response = requests.request(
   "DELETE",
   url,
   auth=auth
)

print(response)