import requests

response = requests.get("https://api.github.com/users")

data = response.json()

print(data[0]["login"])
print(data[0]["node_id"])
print(data[0]["avatar_url"])