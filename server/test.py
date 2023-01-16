import requests
import json



res = requests.post("http://localhost:5000/hit", json.dumps({"data": 90}))
print(res.reason)
print(res.json())