# Webscraping Activité
# Scrapping ac SelectorGadget de google chrome
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

while True : 
    page_events = urlopen("https://allevents.in/paris/all")
    soup = BeautifulSoup(page_events, 'html.parser')
    ##recupere les titres de la page avec l'outil selectorGadget
    title = soup.select(".title h3")
    # Récupérer les titres des activités propres, on utilise l'attribut text et la boucle
    noms_activite = []
    for element in title:
        noms_activite.append(element.text)
    # Renseigne ensuite ce chemin CSS dans la méthode select
    moi = soup.findAll(name = 'span', attrs = {'class':'up-month'})
    jour = soup.findAll(name = 'span', attrs = {'class':'up-day'})
    # Récupérer les titres propres, on utilise l'attribut text et la boucle
    moi_activite = []
    for element in moi:
        moi_activite.append(element.text.strip("()"))
        jour_activite = []
    for element in jour:
        jour_activite.append(element.text.strip("()")[:2])
        
    pages = soup.find('<a href="https://allevents.in/paris/all?page=2"', {'class' :"btn btn-success btn-round btn-large mb20"})*
    if not pages.find('<a href="https://allevents.in/paris/all?page=2"', {'class': 'btn btn-success btn-round btn-large mb20'}):
        
        return url
    else:
        return            






#Note_imdb = Note_imdb[4:]
    

# Création de la data frame

imdb = pd.DataFrame(list(zip(noms_activite,moi_activite,jour_activite)), columns=["Titre","moi","jour"])

print(imdb[:50])


for i range(1,)

