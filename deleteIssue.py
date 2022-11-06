import requests
from requests.auth import HTTPBasicAuth

url = "https://termproject.atlassian.net/rest/api/3/issue/PROJ-5"

auth = HTTPBasicAuth("ozaydine@mef.edu.tr", "q7Ia3tp6AzOaoV6235SeB6CC")

response = requests.request(
   "DELETE",
   url,
   auth=auth
)

print(response)