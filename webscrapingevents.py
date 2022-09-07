from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


page_events=[]
i=1

def get_data(compteur):
    
    page = urlopen("https://allevents.in/paris/all?page="+str(compteur))
    soup = BeautifulSoup(page, 'html.parser')
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
    
    table_activity = pd.DataFrame(list(zip(noms_activite,moi_activite,jour_activite)), columns=["Titre","moi","jour"])
    
    return table_activity


while True:
    result = get_data(i)
    if len(result) > 1:
        page_events.append(result)
        i+=1
    else :
        break
        
    


print(page_events)

