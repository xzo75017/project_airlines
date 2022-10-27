from pymongo import MongoClient

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
        if option == 'Vol':
            self.vol.insert_one(fichier)
        elif option == 'Event':
            self.event.replace_one(fichier, fichier, upsert=True)
        elif option == 'Price':
            self.price.insert_one(fichier)
        elif option == 'Airport':
            self.airport.replace_one(fichier, fichier, upsert=True)
        elif option == 'Airline':
            self.airline.replace_one(fichier, fichier, upsert=True)
        else:
            raise ValueError("L'option n'est pas dans la liste")
    
     
       
       