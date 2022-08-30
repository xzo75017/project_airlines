import requests


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
    print(req.json())  #on affiche le résultat
    
def test_requetes_lufthansa():
        
    token = token_lufthansa()
    base = "https://api.lufthansa.com/v1/"  #lien de base pour toutes les requetes

    #horaire de vol et leur caractéristiques : ici on demande des informations sur les vols des avions de LH, ayant un numéro entre 400 et 405 et entre le 5 et 10 aout , tout les jours
    flight_schedule = "flight-schedules/flightschedules/passenger?airlines=LH&flightNumberRanges=400-405&startDate=05AUG22&endDate=10AUG22&daysOfOperation=1234567&timeMode=UTC"

    #agencement des places assises ainsi que leur caractéristiques : /offers/seatmaps/{flightNumber}/{origin}/{destination}/{departureDate}/{cabinTypeCode}
    seats =  "offers/seatmaps/LH400/FRA/JFK/2014-12-03/C"

    #Caractéristiques des salons disponibles : /offers/lounges/{code}[?][cabinClass={cabinClassCode}|tierCode={tierCode}][&][lang={languageCode}]
    lounges = "offers/lounges/FRA?tierCode=SEN&lang=de"
    
    #Détails d'une ville
    cities = "mds-references/cities?limit=44&offset=123"
    
    print("HORAIRE DE VOL : \n") 
    requete_api_lufthansa(base+flight_schedule, token)

    #print("\n----------------------------------------------------------------------------\n")
    #print("AGENCEMENT DES PLACES ASSISES : \n")
    #requete_api_lufthansa(base+seats,token)

    print("\n----------------------------------------------------------------------------\n")

    print("CARACTERISTIQUES DES SALONS DISPONIBLES : \n")
    requete_api_lufthansa(base+lounges, token)
    
    print("\n----------------------------------------------------------------------------\n")

    print("Villes : \n")
    requete_api_lufthansa(base+cities, token)



#test_requetes_lufthansa()



#----------------------------API BRITISH AIRWAYS --------------------------------

def requete_api_BA(link, token):
    header = {'client-key': token}  #header permettant de s'authentifier
    req = requests.get(link, data=header)   #requete lancée
    print(req)  #on affiche le résultat

def test_requetes_BA():
    base = "https://api.ba.com/rest-v1/v1/"
    token = "6qx5j784nuqwd7h2rs4t9hgg"
    
    #Divertissements disponibles à la date spécifiée
    ife = "ife/?pagename=xml&when=2014-02-15"
    
    #renvoie les offres de forfaits vol + hôtel pour la date de départ souhaitée lorsque les lieux de départ et d'arrivée sont précisés
    HotelPackage = "hotelPackages;origin=LHR;destination=YYZ;departureDate=2014-03-14T12:00:00Z;"
    
    #Renvoie les offres de voitures pour la destination souhaitée pour les dates de prise en charge et de restitution spécifiées
    cars = "cars;destination=MIA;pickUpDate=2014-03-14T12:00:00Z;dropOffDate=2014-03-16T12:00:00Z"
    
    
    requete_api_BA(base+HotelPackage, token)
    
    requete_api_BA(base+cars, token)
    
    
test_requetes_BA()  