from bs4 import BeautifulSoup

with open("C:/Users/alpha/Documents/GitHub/Demo_scraping/BeautifulSoup/formation-scraping.html", "r", encoding="utf-8") as file:
    contenu = file.read()
    
soup = BeautifulSoup(contenu, "html.parser")

print("Titre de la page : ", soup.title.string)

for lien in soup.find_all("a"):
    print("Lien : ", lien.get("href"))