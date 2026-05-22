import requests
url="https://jsonplaceholder.typicode.com/users"
response=requests.get(url)
data=response.json()
print(data)


#post
url="https://jsonplaceholder.typicode.com/posts"
payload={
    "title":"Python",
    "body": "REST API",
    "userId":1
}
response=requests.post(url, json=payload)
print(response.json())

#put
url="https://jsonplaceholder.typicode.com/posts/1"
payload={
 "id":1,
 "title":"Python",
 "body":"Rest API",
 "user_id":1
}
response=requests.put(url, json=payload)
print(response.json())

#patch
url="https://jsonplaceholder.typicode.com/posts"
payload={
    "title": "Partially Updated"
}
response=requests.patch(url, json=payload)
print(response.json())

#delete
url="https://jsonplaceholder.typicode.com/posts/1"
response=requests.delete(url)
print("Status code:", response.status_code)
