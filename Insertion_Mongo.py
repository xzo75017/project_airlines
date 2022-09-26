


def billet_id_split(code):
        temp = code.split(':')
        result = temp[1] + '-' + temp[2]
        result = result.split('-0')[0]
        
        return result

def insertion_mdb_vol(data, db):
        
    nbRequetes = len(data["requetes"])

    for i in range (nbRequetes):
        dict_vol = {}
        list_id = []
        list_dt = []
        list_at = []
        list_dur = []
        list_dac = []
        list_aac = []
        list_ac = []
        
        dict_price = {}
        list_id_price = []
        list_tot = []
        list_AmountPA = []
        list_AmountPC = []
        list_AmountPI = []
        
            #Creation du dictionnaire Vol : 
        for element in (data["requetes"][i]["legs"]):
            list_id.append(billet_id_split(element["id"]))
            list_dt.append(element["departureTime"])
            list_at.append(element["arrivalTime"])
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
        
        #Creation du dictionnaire Price
        
        for element in (data["requetes"][i]["fares"]):
            list_id_price.append(element['tripId'].split(':')[1])
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
        
        for element in (data["requetes"][i]["airports"]):
            db.insert({element["code"]:element["name"]}, 'Airport')
            
        #Insertion dans Airlines si il n'est pas déja présent
        for element in (data["requetes"][i]["airlines"]):
            db.insert({element["code"]:element["name"]}, 'Airline')
        
        #Insertion dans la base MongoDB
            
        db.insert(dict_vol, 'Vol')
        db.insert(dict_price, 'Price')
        
        
        
def insertion_mdb_event(data, db):
    nb_event = len(data['Titre'])
    
    for nom_it, jour_it, mois_it in zip(data['Titre'], data['Jour'], data['Mois']):
        dict = {'Titre':nom_it, 'Jour':jour_it, 'Mois':mois_it, 'Ville':data['Ville'][0]}
        db.insert(dict, 'Event')