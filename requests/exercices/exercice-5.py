import requests

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get("https://formation-scraping.netlify.app/requests", headers=headers)

print(response.text)
print(response.headers)

# Pour retourner le User Agent
print("User Agent envoyé : ", response.request.headers['User-Agent'])