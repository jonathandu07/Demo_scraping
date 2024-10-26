import requests

cookies = {"session_id": "123456"}

reponse = requests.get("https://formation-scraping.netlify.app/requests", cookies=cookies)

print(reponse.cookies)