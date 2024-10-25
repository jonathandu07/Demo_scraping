import requests

data = {'username' : 'bernard', 'password' : 'M0t2p@$$e'}

response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)

print(response.json())