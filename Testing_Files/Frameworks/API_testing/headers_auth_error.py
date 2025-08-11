import requests


headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get("https://api.example.com/data", headers=headers)



response = requests.get("https://api.github.com/users/invaliduser")


if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
