import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get("https://formation-scraping.netlify.app/", headers=headers)

if response.status_code == 200:
    print(response.text)
    
else:
    print(f"Erreur lors de la requête : {response.status_code}")