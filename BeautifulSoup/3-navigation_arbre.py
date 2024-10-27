from bs4 import BeautifulSoup

contenu_html = "<html><body><p>Bonjour</p><p>Au revoir</p></body></html>"

soup = BeautifulSoup(contenu_html, "html.parser")

premiere_balise_p = 