import requests

data = {'name': 'Jacques'}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", data=data )

print(response.status_code)
print(response.json())