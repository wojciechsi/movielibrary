import requests
import json


url = "http://localhost:8080/movies"

payload={}
headers = {
  
}

response = (requests.request("GET", url, headers=headers, data=payload))

data = response.json
print(data)