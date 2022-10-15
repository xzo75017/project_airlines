from platform import python_build
import requests
import json
from pprint import pprint
import pandas as pd
import gestion_fichiers


def write_file(titre, file):
    with open('requetes/' + titre + '.json', 'w') as f:
        json.dump(file, f)
        
#----------------------------API flightapi --------------------------------
def requete_api_flightapi(operation, filter):
    '''
    Fonction permettant de lancer une requete sur l'API de flightapi.
    Paramètres : 
        -filtre (par exemple : PAR/LIS/2022-10-15/2/0/1/Economy/EUR pour un voyage aller de paris à lisbonne)
        -operation permettant de savoir si c'est un allé simple ou aller retour
    '''
    
    token = '632475da784cd8f66841cac4'
    base = "https://api.flightapi.io/"
    
    link = base + operation + '/' + token + '/' + filter
    
    req = requests.get(link)   #requete lancée
    return req.json()  #on affiche le résultat



    
