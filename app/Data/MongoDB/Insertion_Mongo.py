

def billet_id_split(code):
    '''
    Fonction premettant de formatter l'id de "legs"
    '''
    temp = code.split(':')
    result = temp[1] + '-' + temp[2]
    result = result.split('-0')[0]
    
    return result

def insertion_mdb_vol(data, db):
    
    '''
    Fonction permettant de récupérer les données d'un json et insérer dans les bonnes collections dans MongoDB
    Paramètre:
    -data : fichier contenant les informations de vols
    -db : connexion au MongoDB
    '''
    nbRequetes = len(data["requetes"])
    dict_vol = {}
    list_id = []
    list_dt = []
    list_at = []
    list_dur = []
    list_dac = []
    list_aac = []
    list_ac = []
    list_depdate = []
    list_arrdate = []
    
    dict_price = {}
    list_id_price = []
    list_tot = []
    list_AmountPA = []
    list_AmountPC = []
    list_AmountPI = []
    
        #Creation du dictionnaire Vol : 
    for element in (data["requetes"][nbRequetes-1]["legs"]):
        list_id.append(billet_id_split(element["id"]))
        list_dt.append(element["departureTime"] + ':00')
        list_at.append(element["arrivalTime"] + ':00')
        list_depdate.append(element['departureDateTime'].split('T')[0])
        list_arrdate.append(element['arrivalDateTime'].split('T')[0])
        list_dur.append(element["duration"])
        list_dac.append(element["departureAirportCode"])
        list_aac.append(element["arrivalAirportCode"])
        list_ac.append(element["airlineCodes"])
    
            
    dict_vol["id"] = list_id
    dict_vol["departureTime"] = list_dt
    dict_vol["arrivalTime"] = list_at 
    dict_vol["duration"] = list_dur 
    dict_vol["departureAirportCode"] = list_dac 
    dict_vol["arrivalAirportCode"] = list_aac 
    dict_vol["airlineCodes"] = list_ac
    dict_vol["departureDate"] = list_depdate
    dict_vol["arrivalDate"] = list_arrdate   
    
    #Creation du dictionnaire Price
    
    for element in (data["requetes"][nbRequetes-1]["fares"]):
        split_id = element['tripId'].split(':')[1]   #On split par rapport au ":" pour obtenir un id ressemblant à l'id de vol
        resplit_id = split_id.split('-')   #Il arrive que l'id soit encore différent, il faut donc transformer ça une 2e fois
        if len(resplit_id) > 2:
            list_id_price.append(split_id.split('-')[0]+ '-' + split_id.split('-')[1])
        else:
            list_id_price.append(split_id)
        list_tot.append(element['price']['totalAmount'])
        list_AmountPA.append(element['price']['amountPerAdult'])
        list_AmountPC.append(element['price']['amountPerChild']) 
        list_AmountPI.append(element['price']['amountPerInfant'])
    
    dict_price["id"] = list_id_price
    dict_price["totalAmount"] = list_tot
    dict_price["amountPerAdult"] = list_AmountPA
    dict_price["amountPerChild"] = list_AmountPC
    dict_price["amountPerInfant"] = list_AmountPI
    
    #Insertion dans Airports si il n'est pas déja présent
    
    for element in (data["requetes"][nbRequetes-1]["airports"]):
        db.insert({element["code"]:element["name"]}, 'Airport')
        
    #Insertion dans Airlines si il n'est pas déja présent
    for element in (data["requetes"][nbRequetes-1]["airlines"]):
        db.insert({element["code"]:element["name"]}, 'Airline')

        
    
    #Insertion dans la base MongoDB
        
    db.insert(dict_vol, 'Vol')
    db.insert(dict_price, 'Price')
    
        
        
def insertion_mdb_event(data, db):
    '''
    Fonction permettant de récupérer les données d'un json et insérer dans la collection event dans MongoDB
    Paramètre:
    -data : fichier contenant les informations des evenements
    '''
    
    for nom_it, jour_it, mois_it in zip(data['Titre'], data['Jour'], data['Mois']):
        dict = {'Titre':nom_it, 'Jour':jour_it, 'Mois':mois_it, 'Ville':data['Ville'][0]}
        db.insert(dict, 'Event')