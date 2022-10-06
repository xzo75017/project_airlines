from operator import itemgetter
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from gestion_fichiers import Fichier
from DB_Mongo import DB_Mongo
from Insertion_Mongo import insertion_mdb_event
import json


#page_events=[]
i=1
table_activity = pd.DataFrame(columns=["Titre","Mois","Jour", "Ville"])
ville = "Paris"
    

def get_data(compteur):
    
    page = urlopen("https://allevents.in/" + ville + "/all?page="+str(compteur))
    soup = BeautifulSoup(page, 'html.parser')
    ##recupere les titres de la page avec l'outil selectorGadget
    title = soup.select(".title h3")
    # Récupérer les titres propres, on utilise l'attribut text et la boucle
    # Renseigne ensuite ce chemin CSS dans la méthode select
    mois = soup.findAll(name = 'span', attrs = {'class':'up-month'})
    jour = soup.findAll(name = 'span', attrs = {'class':'up-day'})
    # Récupérer les titres des activités propres, on utilise l'attribut text et la boucle
    noms_activite = []
    mois_activite = []
    jour_activite = []
    for nom_it, mois_it, jour_it in zip(title, mois, jour) :
        noms_activite.append(nom_it.text)
        mois_activite.append(mois_it.text.strip("()"))
        jour_activite.append(jour_it.text.strip("()")[:2])
        
    result = pd.DataFrame(list(zip(noms_activite,mois_activite,jour_activite)), columns=["Titre","Mois","Jour"])
    
    return result


while True:
    result = get_data(i)
    if len(result) > 1:
        table_activity = pd.concat([table_activity, result])
        i+=1
    else :
        break
        
table_activity['Ville'] = ville    

dict = table_activity.to_dict(orient='list')

io = open(Fichier('event', dict, ville).link, "r")
data = json.load(io)
db = DB_Mongo()  
insertion_mdb_event(data, db)