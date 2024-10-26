import requests

response = requests.get("https://formation-scraping.netlify.app/requests")

if response.status_code == 200:
    print("Requête réussie. Voici le contenu de la page :")
    print(response.text)
    
else:
    print(f"Erreur lors de la requête, code de statut : {response.status_code}")