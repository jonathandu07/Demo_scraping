import requests


try:
    response = requests.get("https://formation-scraping.netlify.app/", timeout=5)
    
    if response.status_code == 200:
        print("Requête réussie. Voici le contenu de la page :")
        print(response.text)
    else:
        print(f"Erreur lors de la requête, code de statut : {response.status_code}")
        
except requests.exceptions.Timeout:
    print("La requête a expiré. Le serveur a mis trop de temps à répondre.")