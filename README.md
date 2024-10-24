# Projet de Collecte de Données Touristiques

## Introduction
Ce projet a pour objectif de collecter des données touristiques à partir du site [Bordeaux Tourisme](https://www.bordeaux-tourisme.com) afin d'enrichir des informations disponibles. Les données collectées seront stockées dans une base de données DuckDB.

## Structure du Projet
1. Le projet est organisé comme suit :
  ```bash
  ├── README.md 
  ├── scripts/   ├── scrape_list.py # Script pour récupérer une liste d'informations │ 
  │              ├── scrape_details.py # Script pour explorer les détails de chaque lien 
  │              └── tourisme.db # Base de données DuckDB    
  └── README
  ```


## Installation
Pour exécuter ce projet, suivez ces étapes :
1. Clonez le dépôt : 
   ```bash
   git clone <https://github.com/Gregoire-Mouilleau/Atelier2.git>
   ```

2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt

3. Exécutez les scripts :
   ```bash
   python scripts/scrape_list.py
   python scripts/scrape_details.py
