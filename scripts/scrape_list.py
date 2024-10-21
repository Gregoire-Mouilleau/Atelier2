import requests
from bs4 import BeautifulSoup

url = "https://www.bordeaux-tourisme.com/votre_lien_ici"  # Remplacez avec l'URL appropriée
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Exemple de récupération d'informations
items = soup.find_all("div", class_="item-class")  # Modifiez selon la structure du site
for item in items:
    print(item.text)  # Remplacez avec l'attribut que vous souhaitez extraire
