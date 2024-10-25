import requests

try:
    response = requests.get("https://127.0.0.1:5000", verify=False)
    
    if response.status_code == 200:
        print("Connexion réussie, réponse du serveur :")
        print(response.text)
    else:
        print(f"Erreur lors de la requête, statut : {response.status_code}")
        
except requests.exceptions.SSLError as e:
    print(f"Erreur SSL : {str(e)}")