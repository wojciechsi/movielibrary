import requests
import json


payload = ""
headers = {
  'Content-Type': 'application/json'
}

for i in  range(5, 7):
    number = i
    url = "http://localhost:8080/movies/" + str(number)
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print("DELETION OF " + str(number) + " STATUS: " + response.text)
    i += 1

