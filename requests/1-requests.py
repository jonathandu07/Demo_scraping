# Tester si cela fonctionne bien :-)

# Importation de la bibliothèque requests.

import requests

response = requests.get("https://formation-scraping.netlify.app/")

print(response.text)