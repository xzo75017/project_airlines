from pymongo import MongoClient
import json

class DB_Mongo:
    
    connect = ''
    vol = ''
    event = ''
    
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

    
    def insert_vol(self, fichier):
       self.vol.insert_one(fichier) 
    
    def insert_event(self, fichier):
       self.event.insert_one(fichier) 
       
       