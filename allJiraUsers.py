import requests
import json
url="https://termproject.atlassian.net/rest/api/2/users/search"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
response=requests.get(url,headers=headers,auth=("ozaydine@mef.edu.tr","Wjs8qOB4SKSoZyDp0dax400A"))
data=response.json()
print(len(data))
print(data)
for users in data:
    print(users["displayName"])