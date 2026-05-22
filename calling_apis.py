import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()
print(data[0]["name"])

# Calling API using Python requests
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()
print("First User Name:", data[0]["name"])
print("Email:", data[0]["email"])