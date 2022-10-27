from sql_database import table_association, DB_SQL_connect, insertion_vol, insertion_event
from dash import dash_table
import pandas as pd
from datetime import timedelta as td, datetime as dt
from API_flightapi.API_flightapi import requete_api_flightapi
from Data.json.gestion_fichiers import Fichier
from Data.MongoDB.DB_Mongo import DB_Mongo
from Data.MongoDB.Insertion_Mongo import insertion_mdb_vol, insertion_mdb_event
from allevents.webscrapingevents import scrap
import json

def isMoreThan7Days(date_scrap):
    '''
    Renvoie True si la date d'aujourd'hui est à plus de 7 jours de la date de paramètre, False sinon
    Paramètre:
    -Date comparée à aujourd'hui
    Sortie:
    -booléen
    '''
    # print("dernier scrap : " + date_scrap)
    date_object = dt.fromisoformat(date_scrap)
    if dt.now() < date_object + td(days=7):  #Si la date d'aujourd'hui est inférieur au last scrap + 7 jours
        return False
    else:
        return True
    
def dash_event(date):
    '''
    Fonction permettant au dash de récupérer des évenements contenues entre 2 dates
    '''
    # print("Entrée dans la fonction dash_event")
    with DB_SQL_connect().connect() as connection:
        # print("connexion ouverte")
        ville = date[0][2]
        result = connection.execute("Select Events.Last_Scrap FROM Events WHERE Events.city = (?)", ville)
        retour = result.fetchone()
        if type(retour) == type(None) or isMoreThan7Days(retour[0]):
            # print("La ville n'est pas dans la base ou cela fait + de 7j")
            # print("Quelle est la ville? : ", ville)
            io = open(Fichier('event', scrap(ville), ville_arr=ville).link, "r")
            data = json.load(io)
            # print("Le fichier json vient d'être créé")
            db = DB_Mongo()  
            insertion_mdb_event(data, db)
            # print("Les données sont bien insérés dans le MongoDB")
            insertion_event(db, ville)
            # print("Les données sont bien insérés dans le SQL")    
        return table_event(connection, date)
    
    
def creation_dash_table(data):
    '''
    Fonction permettant de créer une dashtable à partir de données
    Paramètre :
    -data : liste de données
    
    Sortie : 
    -dash_table
    '''
    df1 = pd.DataFrame(data)
    return [
       dash_table.DataTable(
            df1.to_dict('records'),
            [{"name": i, "id": i} for i in df1.columns],
            fill_width=False,
            page_size = 10
            
       ) 
       
    ]
    
def date_range(start, end):
    '''
    Fonction permettant de lister les jours entre 2 dates.
    Paramètres :
    -start : date de départ
    -end : date de fin
    Sortie :
    liste des jours entre les 2 dates
    '''
    delta = end - start  # as timedelta
    days = [start + td(days=i) for i in range(delta.days + 1)]
    return days


def table_event(cursor, date):
    '''
    Fonction permettant de récupérer les évenements entre 2 dates données.
    
    Paramètres :
    -cursor : connexion à la DB
    -date : liste de Tuples de date de forme [(mois, jour, ville)]
    
    Sortie :
    Liste d'evenement contenue entre 2 dates
    '''
    ins = 'SELECT events.title, events.day, events.month FROM events WHERE (events.month,events.day, events.city) = ((?,?,?))'
    retour = []
    for i in range (len(date)):
        result = cursor.execute(ins, date[i])
        retour.extend(result.fetchall())
    return retour


def city_to_code(ville):
    '''
    Fonction renvoyant le code IATA de la ville rentrée en paramètre
    Paramètres:
    -ville : Nom de la ville
    Sortie :
    -Code IATA associé à la ville
    '''
    with DB_SQL_connect().connect() as connection:
        filter = ville + '%'
        ins = 'Select City.cityCode from City WHERE City.cityName LIKE (?)'
        result = connection.execute(ins, filter)
        retour = result.fetchone()
        if type(retour)==type(None):
            return 0
        else:
            return retour[0]

def data_handler_vol(depart, arrivee, code_dep, code_arr, start_date, adulte, enfant, bebe):
    '''
    Automatisation de la requete de Vol.
    Paramètres :
    -depart : Ville de départ
    -arrivee : Ville d'arrivée
    -code_dep : code IATA de la ville de départ
    -code_arr : code IATA de la ville d'arrivée
    -start_date : Date du vol
    -adulte : nombre d'adultes
    -enfant : nombre d'enfants
    -bebe : nombre de bébés
    Sortie :
    -Résultat de la recherche SQL contenant les données recherchées
    '''
    # print("La fonction est rentrée dans data_handler")
    filter = code_dep + '/' + code_arr + '/' + start_date + '/' + str(adulte) + '/' + str(enfant) + '/' + str(bebe) + '/' + 'Economy' + '/' + 'EUR'
    operation = 'onewaytrip'
    reponse = requete_api_flightapi(operation, filter)
    # print("La requete a bien été faite")
    lien = Fichier(operation, reponse, ville_dep=depart, ville_arr=arrivee).link
    io = open(Fichier(operation, reponse, ville_dep=depart, ville_arr=arrivee).link, "r")
    data = json.load(io)
    # print("Le fichier json vient d'être créé avec le lien : ", lien)
    db = DB_Mongo()  
    insertion_mdb_vol(data, db)
    # print("Les données sont bien insérés dans le MongoDB")
    insertion_vol(db)
    # print("Les données sont bien insérés dans le SQL")
    with DB_SQL_connect().connect() as connection:
        return table_association(connection, depart, arrivee, start_date)
    
    
    
    
    
    
    
    
    