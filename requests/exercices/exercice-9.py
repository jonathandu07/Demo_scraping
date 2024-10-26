import requests

try:
    response = requests.get("https://formation-scraping.netlify.app/requests", timeout=0.1)
    print(response.status_code)
    print(response.text)
    
except requests.exceptions.Timeout:
    print("La requête a expiré !")