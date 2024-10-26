import requests # Importation du module requests

# Création de la variable response pour envoyer yne requête GET à l'URL spécifiée
response = requests.get("https://formation-scraping.netlify.app/requests")

# Afficher le résultat/contenu du code HTML
print(response.text)