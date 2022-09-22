from datetime import datetime
import json

class Fichier:
    data = ''
    param = ''
    link = ''
    def __init__(self, param, data):
        self.param = param
        
        self.link = "requetes/"+ param + "/Requete-du-" + datetime.now().strftime("%d-%m-%Y") + ".json"
        
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

            


