import requests

response = requests.get("https://api.github.com/users")

print(response.status_code)
# print(response.text)

# print only first 200 characters (slicing)

print(response.text[:2])

print(response.json())