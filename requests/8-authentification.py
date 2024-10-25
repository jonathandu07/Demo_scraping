from requests.auth import HTTPBasicAuth
import requests

response = requests.get("http://127.0.0.1:5000", auth=HTTPBasicAuth('username', 'password'))

if response.status_code == 200:
    print("Authentification réussie : ", response.text)
else:
    print(f"Authentification échouée. Statut : {response.status_code}")