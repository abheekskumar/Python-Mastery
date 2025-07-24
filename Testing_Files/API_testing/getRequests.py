import requests , json


response = requests.get("https://api.github.com/users/abheekskumar")
data = response.json()

print(data["name"])
print(data["public_repos"])
print(data["bio"])
with open("test.json","w") as fh:
    fh.write(json.dumps(data,indent = 4))