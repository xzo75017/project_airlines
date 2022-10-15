from msilib.schema import Error
from pymongo import MongoClient
import json

class DB_Mongo:
    
    connect = ''
    vol = ''
    event = ''
    price = ''
    airport = ''
    airline = ''
    
    def connexion(self):
        '''
        Connexion au serveur MongoDB
        '''
        client = MongoClient("mongodb+srv://DST-PROJECT:DST@cluster0.7wo11db.mongodb.net/?retryWrites=true&w=majority")
        return client
    
    def __init__(self):
        self.connect = self.connexion().test
        self.vol = self.connect['Vol']
        self.event = self.connect['Event']
        self.price = self.connect['Price']
        self.airport = self.connect['Airport']
        self.airline = self.connect['Airline']
        

    
    def insert(self, fichier, option):
        match option:
            case 'Vol':
                self.vol.insert_one(fichier)
            case 'Event':
                self.event.insert_one(fichier)
            case 'Price':
                self.price.insert_one(fichier)
            case 'Airport':
                self.airport.replace_one(fichier, fichier, upsert=True)
            case 'Airline':
                self.airline.replace_one(fichier, fichier, upsert=True)
            case other:
                raise ValueError("L'option n'est pas dans la liste")
    
     
       
       