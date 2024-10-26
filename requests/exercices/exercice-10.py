import requests

reponse = requests.get("https://formation-scraping.netlify.app/requests", allow_redirects=True)

print("URL finale après redirection :", reponse.url)

for redirection in reponse.history:
    print("Reddirection : ", redirection.status_code, redirection.url)