import requests
from bs4 import BeautifulSoup
import duckdb

conn = duckdb.connect('tourisme.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS informations_touristiques (
    id INTEGER PRIMARY KEY,
    titre VARCHAR,
    description TEXT,
    lien VARCHAR
);
''')

urls = [
    "https://www.bordeaux-tourisme.example" 
]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all("div", class_="item-class")  
    for item in items:
        titre = item.find("h2").text 
        description = item.find("p").text 
        lien = item.find("a")["href"]

        conn.execute('''
        INSERT INTO informations_touristiques (titre, description, lien)
        VALUES (?, ?, ?);
        ''', (titre, description, lien))

conn.close()
