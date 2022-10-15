from sql_database import table_association, DB_SQL_connect
from dash import dash_table
import pandas as pd
from datetime import timedelta as td

def dash_vol(donnee):
    '''
    Fonction permettant au dash d'avoir accés à la table d'association vol
    '''
    with DB_SQL_connect().connect() as connection:
        return table_association(connection)
    
def dash_event(date):
    '''
    Fonction permettant au dash de récupérer des évenements contenues entre 2 dates
    '''
    with DB_SQL_connect().connect() as connection:
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
    print(df1.head())
    return [
       dash_table.DataTable(
            df1.to_dict('records'),
            [{"name": i, "id": i} for i in df1.columns],
            fill_width=False
            
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
    ins = 'SELECT * FROM events WHERE (events.month,events.day, events.city) = ((?,?,?))'
    retour = []
    for i in range (len(date)):
        result = cursor.execute(ins, date[i])
        retour.extend(result.fetchall())
    return retour