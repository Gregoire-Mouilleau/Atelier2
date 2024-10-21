import requests
from bs4 import BeautifulSoup

# Exemple d'URL à partir de laquelle vous voulez extraire des détails
url = "https://www.bordeaux-tourisme.com/votre_lien_de_detail"  # Remplacez avec l'URL appropriée
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Exemple de récupération d'informations détaillées
details = soup.find("div", class_="details-class")  # Modifiez selon la structure du site
print(details.text)  # Remplacez avec l'attribut que vous souhaitez extraire
