from DB_Mongo import DB_Mongo

db = DB_Mongo()

db1 = db.connexion()
db2 = db1.test
collection = db2["vol"]  
cursor = collection.find()


for item in cursor:
    print(type(item))
    
    id_vol = item.get('id')
    print(id_vol)
    
    departureTime = item.get('departureTime')
    arrivalTime = item.get('arrivalTime')
    duration = item.get('duration')
    departureAirportCode = item.get('departureAirportCode')
    arrivalAirportCode = item.get('arrivalAirportCode')
    airlineCodes = item.get('airlineCodes')
    departureDate = item.get('departureDate')
    arrivalDate = item.get('arrivalDate')
    for id_vol_it,departureTime_it,arrivalTime_it,duration_it,departureAirportCode_it,arrivalAirportCode_it,airlineCodes_it, departureDate_it, arrivalDate_it in zip(id_vol,departureTime,arrivalTime,duration,departureAirportCode,arrivalAirportCode,airlineCodes,departureDate, arrivalDate) :
        airlineCodes_it =  ', '.join(airlineCodes_it)
        
collection2 = db2["price"]  
cursor2 = collection2.find()
   
for i in cursor2:
    print(type(i))
    id_price = i.get('id')
    totalAmount = i.get('totalAmount')
    amountPerAdult = i.get('amountPerAdult')
    amountPerChild = i.get('amountPerChild')
    amountPerInfant = i.get('amountPerInfant')
    print(id_price)
    for id_price_it,totalAmount_it,amountPerAdult_it,amountPerChild_it,amountPerInfant_it in zip(id_price,totalAmount,amountPerAdult,amountPerChild,amountPerInfant) :
        cur.execute("insert into price(id_price,totalAmount,amountPerAdult,amountPerChild,amountPerInfant) values (?,?,?,?,?)" , (id_price_it,totalAmount_it,amountPerAdult_it,amountPerChild_it,amountPerInfant_it))

collection3 = db2["events"]  
cursor3 = collection3.find()
   
for i in cursor3:
    titre = i.get('Titre')
    jour = i.get('Jour')
    mois = i.get('Mois')
    ville = i.get('Ville')
    cur.execute("insert into eventss (title,day,month,city) values (?,?,?,?)" , (titre,jour,mois,ville))
    
collection4 = db2["airport"]  
cursor4 = collection4.find()
 
for i in cursor4:
    codeNameAirport = list(i.keys())[0]
    airportName = list(i.values())[0]
    print(airportName)
    cur.execute("insert into airport (airportCode, airportName) values (?, ?);" , (codeNameAirport, airportName))
    
collection5 = db2["airline"]  
cursor5 = collection4.find()

key= '_id'

for i in cursor5:
    del cursor5[i][key]
    
for i in cursor5:
    codeNameAirline = list(i.keys())[0]
    airlineName = list(i.values())[0]
    cur.execute("insert into airline (airlineCode, airlineName) values (?, ?);" , (codeNameAirline, airlineName))

    