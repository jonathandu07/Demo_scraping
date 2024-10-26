import requests

response = requests.get("https://formation-scraping.netlify.app/requests")

start = response.text.find("L'Ardèche")
end = response.text.find("</p>", start)

description = response.text[start:end]

print(description)