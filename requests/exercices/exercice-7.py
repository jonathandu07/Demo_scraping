import requests

response = requests.get("https://formation-scraping.netlify.app/requests")

debut = response.text.find("Temps de visite conseillé")

fin = response.text.find("</td>",debut)

dure_visite = response.text[debut:fin]

print(dure_visite)
