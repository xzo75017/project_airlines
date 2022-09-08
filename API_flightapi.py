from platform import python_build
import requests
import json
from pprint import pprint
import pandas as pd
import sqlite3

def connexion():
    '''
    Connexion au serveur MongoDB
    '''
    client = MongoClient("mongodb+srv://DST-PROJECT:DST@cluster0.7wo11db.mongodb.net/?retryWrites=true&w=majority")
    return client

def write_file(titre, file):
    with open('requetes/' + titre + '.json', 'w') as f:
        json.dump(file, f)
        
#----------------------------API flightapi --------------------------------
def requete_api_flightapi(link):
    '''
    Fonction permettant de lancer une requete sur l'API de flightapi.
    Paramètres : 
        -Lien décrivant la requete (par exemple : https://api.lufthansa.com/v1/offers/lounges/FRA?tierCode=SEN&lang=de pour les lounges)
        -token permettant de s'authentifier
    '''
    req = requests.get(link)   #requete lancée
    return req.json()  #on affiche le résultat


def test_requetes_flightapi():
        
    token = '6319f17afeb58fcca731e7a0'
    operation = 'onewaytrip/'
    filter = "/PAR/LIS/2022-10-15/2/0/1/Economy/EUR"
    base = "https://api.flightapi.io/"+ operation + token + filter   #lien de base pour toutes les requetes

    #horaire de vol et leur caractéristiques : ici on demande des informations sur les vols des avions de LH, ayant un numéro entre 400 et 405 et entre le 5 et 10 aout , tout les jours
    #flight_schedule = "flight-schedules/flightschedules/passenger?airlines=LH&flightNumberRanges=400-405&startDate="+datedepart+"&endDate="+datearrive+"&daysOfOperation=1234567&timeMode=UTC"
    schedule = "&flight_date=2019-02-31"
    
    reponse = requete_api_flightapi(base)
    #pprint (reponse)
    
    write_file('flightapi_schedule', reponse)
    
    return reponse

    



def main():            #Ecrire + lire json en meme temps pour optimiser
    data = test_requetes_flightapi()
    df = pd.DataFrame(data['legs'])
    print(df.head(10))
    
    
    
    
if __name__=="__main__":
    main()