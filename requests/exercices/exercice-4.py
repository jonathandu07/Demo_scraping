import requests

params = {"query": "tourisme"}

response = requests.get("https://formation-scraping.netlify.app/requests", params=params)

print(response.url)