from bs4 import BeautifulSoup

soupe = BeautifulSoup("<html><body><p>Bonjour</p></body></html>", "html.parser")

print(soupe.prettify())