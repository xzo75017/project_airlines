import requests
import json


#----------------------------API LUFTHANSA --------------------------------

def token_lufthansa():
    '''
    Fonction permettant d'obtenir un token pour s'authentifier à l'API de lufthansa.
    retourne un token en format json
    '''
    url = "https://api.lufthansa.com/v1/oauth/token"       #url pour post une demande de token
    header_auth = {'client_id':'fuf4333jnbsfp63vdc248rxq', 'client_secret':'bfQKjgnQMQBTxtXMGtpq', 'grant_type':'client_credentials'}  #header avec l'id, le mdp (secret) et grant_type
    token = requests.post(url, data=header_auth)    #demande de token
    return token.json()  #on transforme le token en json pour lire et récuperer les infos plus facilement

def requete_api_lufthansa(link, token):
    '''
    Fonction permettant de lancer une requete sur l'API de lufthansa.
    Paramètres : 
        -Lien décrivant la requete (par exemple : https://api.lufthansa.com/v1/offers/lounges/FRA?tierCode=SEN&lang=de pour les lounges)
        -token permettant de s'authentifier
    '''
    header = {'Authorization':'Bearer ' + token['access_token'], 'Accept': 'application/json'}  #header permettant de s'authentifier
    req = requests.get(link, headers=header)   #requete lancée
    #return req.json()  #on affiche le résultat
    print(req.json())
    
def test_requetes_lufthansa(datedepart, datearrive):
        
    token = token_lufthansa()
    base = "https://api.lufthansa.com/v1/"  #lien de base pour toutes les requetes

    #horaire de vol et leur caractéristiques : ici on demande des informations sur les vols des avions de LH, ayant un numéro entre 400 et 405 et entre le 5 et 10 aout , tout les jours
    flight_schedule = "flight-schedules/flightschedules/passenger?airlines=LH&flightNumberRanges=400-405&startDate="+datedepart+"&endDate="+datearrive+"&daysOfOperation=1234567&timeMode=UTC"
    
    print("HORAIRE DE VOL : \n") 
    reponse = requete_api_lufthansa(base+flight_schedule, token)
    
    with open('vol.json', 'w') as f:
        json.dump(reponse, f)



def main():
    datedep="05AUG22"
    datend="10AUG22"
    test_requetes_lufthansa(datedep, datend)
    
    
if __name__=="__main__":
    main()



