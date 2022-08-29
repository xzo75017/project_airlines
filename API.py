import requests



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


def requete_api_BA(link, token):
    header = {'client-key': token}  #header permettant de s'authentifier
    req = requests.get(link, data=header)   #requete lancée
    print(req)  #on affiche le résultat

def test_requetes_BA():
    base = "https://api.ba.com/rest-v1/"
    token = "6qx5j784nuqwd7h2rs4t9hgg"
    
    #Divertissements disponibles à la date spécifiée
    ife = "v1/ife/?pagename=xml&when=2014-02-15"
    
    #Renvoie le prix le plus bas sur l'itinéraire spécifié sur une période d'un mois ou de 12 mois
    flightOfferBasic = "v1/flightOfferBasic;departureCity=LON;arrivalCity=NYC;cabin=economy;journeyType=roundTrip;range=yearLow"
    
    #Vols au départ de LHR entre 6h00 et 11h00 heure locale.
    flight = "v1/flights;departureLocation=LHR;startTime=06:00;endTime=11:00"
    
    
    requete_api_BA(base+flightOfferBasic, token)
    
    requete_api_BA(base+flight, token)
    
    
test_requetes_BA()  