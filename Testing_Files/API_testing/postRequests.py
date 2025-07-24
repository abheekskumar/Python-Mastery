import requests, json

url = "https://httpbin.org/post"
payload = {"username":"testing","score":23}

response = requests.post(url,json = payload)
print(response.json())