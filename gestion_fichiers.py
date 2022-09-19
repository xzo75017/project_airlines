from datetime import datetime
import json

class Fichier:
    data = ''
    param = ''
    listObj = []
    
    def __init__(self, param, data):
        self.param = param
        
        link = "requetes/"+ param + "/Requete-du-" + datetime.now().strftime("%d-%m-%Y") + ".json"
        
        try:
            #Si le fichier existe, on rajoute l'objet json dans le fichier correspondant
            fp = open(link, 'r+')
            merge = json.load(fp)
            merge["requetes"].append(data)
            fp.seek(0)
            json.dump(merge, fp)
            self.listObj = merge
        except IOError:
        # If not exists, create the file
            fp = open(link, 'w+')
            prefix = {"requetes":[]}
            prefix["requetes"].append(data)
            json.dump(prefix, fp)
            self.listObj = data

            


