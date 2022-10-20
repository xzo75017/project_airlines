from datetime import datetime
import json
from pathlib import Path

class Fichier:
    param = ''
    link = ''
    def __init__(self, param, data, ville_dep = '', ville_arr = ''):
        self.param = param
        
        if param == 'event':   #Si les données contiennent des evenements, on va les stocker dans le dossier evenement
            self.link = "app/Data/json/evenements/"+ ville_arr + "/Requete-du-" + datetime.now().strftime("%d-%m-%Y") + ".json"
            Path("app/Data/json/evenements/"+ ville_arr).mkdir(parents=True, exist_ok=True)
            self.json_event(data)
        else:              #sinon ce sont des requetes, dans le dossier requetes
            self.link = "app/Data/json/requetes/"+ param + "/" + ville_dep + "-" + ville_arr + "/Requete-du-" + datetime.now().strftime("%d-%m-%Y") + ".json"
            Path("app/Data/json/requetes/"+ param + "/" + ville_dep + "-" + ville_arr).mkdir(parents=True, exist_ok=True)
            self.json_vol(data)
        

            
    def json_vol(self, data):
        try:
            #Si le fichier existe, on rajoute l'objet json dans le fichier correspondant
            fp = open(self.link, 'r+')
            merge = json.load(fp)
            merge["requetes"].append(data)
            fp.seek(0)
            json.dump(merge, fp)
        except IOError:
        # If not exists, create the file
            fp = open(self.link, 'w+')
            prefix = {"requetes":[]}
            prefix["requetes"].append(data)
            json.dump(prefix, fp)
            
    def json_event(self, data):
        #créer le fichier dans evenement pour une ville
        fp = open(self.link, 'w+')
        json.dump(data, fp)
