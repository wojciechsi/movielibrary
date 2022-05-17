import requests
import json

url = "http://localhost:8080/movies"

payload = json.dumps([
  {
    "name": "Czas Apokalipsy",
    "rating": 7
  }
])
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)