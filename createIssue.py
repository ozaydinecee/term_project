import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://termproject.atlassian.net/rest/api/2/issue"

auth = HTTPBasicAuth("ozaydine@mef.edu.tr", "q7Ia3tp6AzOaoV6235SeB6CC")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
payload = json.dumps(
    {
        "fields": {
            "project":
                {
                    "key": "PROJ"
                },
            "summary": "MEF University issue",
            "description": "Creating of an issue using project keys and issue type names using the REST API",
            "issuetype": {
                "name": "Task"
            }
        }
    }
)
response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)
print(response.text,response)
