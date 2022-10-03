def insertion_sql_vol():
    for item in jdata:
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
            db_cursor.execute("insert into vol(id_vol,departureTime,arrivalTime,duration,departureAirportCode,arrivalAirportCode,airlineCodes,departureDate, arrivalDate) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)ON DUPLICATE KEY UPDATE id_vol = %s;", (id_vol_it,departureTime_it,arrivalTime_it,duration_it,departureAirportCode_it,arrivalAirportCode_it,airlineCodes_it,departureDate_it, arrivalDate_it, id_vol_it))
    conn_object.commit()
    
db_cursor.execute("SELECT * FROM vol LIMIT 20;")
db_cursor.fetchall()
def insertion_sql_price():
    for i in jdata2:
        print(type(item))
        id_price = item.get('id')
        totalAmount = i.get('totalAmount')
        amountPerAdult = i.get('amountPerAdult')
        amountPerChild = i.get('amountPerChild')
        amountPerInfant = i.get('amountPerInfant')
        for id_price_it,totalAmount_it,amountPerAdult_it,amountPerChild_it,amountPerInfant_it in zip(id_price,totalAmount,amountPerAdult,amountPerChild,amountPerInfant) :
            db_cursor.execute("insert into price(id_price,totalAmount,amountPerAdult,amountPerChild,amountPerInfant) values (%s,%s,%s,%s,%s)" , (id_price_it,totalAmount_it,amountPerAdult_it,amountPerChild_it,amountPerInfant_it))
result = db_cursor.execute("SELECT * FROM price LIMIT 10;")
print(type(result))

db_cursor.execute("SELECT * FROM price LIMIT 20;")
db_cursor.fetchall()
def insertion_sql_eventss():
    for i in jdata3:
        titre = i.get('Titre')
        jour = i.get('Jour')
        mois = i.get('Mois')
        ville = i.get('Ville')
        print(ville)
        db_cursor.execute("insert into eventss (title,day,month,city) values (%s,%s,%s,%s)" , (titre,jour,mois,ville))
    

db_cursor.execute("SELECT * FROM eventss LIMIT 20;")
db_cursor.fetchall()
def insertion_sql_airport():
    key= '_id'
    for i in range(len(jdata4)):
        del jdata4[i][key]
    for i in jdata4:
        codeNameAirport = list(i.keys())[0]
        airportName = list(i.values())[0]
        print(airportName)
        db_cursor.execute("insert into airport (airportCode, airportName) values (%s, %s);" , (codeNameAirport, airportName))
    
    db_cursor.execute("SELECT airportCode FROM airport;")
    db_cursor.fetchall()

def insertion_sql_airline():
    key= '_id'
    for i in range(len(jdata5)):
        del jdata5[i][key]
    for i in jdata5:
        codeNameAirline = list(i.keys())[0]
        airlineName = list(i.values())[0]
        print(airlineName)
        db_cursor.execute("insert into airline (airlineCode, airlineName) values (%s, %s);" , (codeNameAirline, airlineName))
    

db_cursor.execute("SELECT * FROM airline LIMIT 20;")
db_cursor.fetchall()
