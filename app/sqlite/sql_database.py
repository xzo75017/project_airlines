from sqlalchemy import Table, create_engine, MetaData, String, Column, Float


def DB_SQL_connect():
    return create_engine('sqlite:///app/sqlite/database/travel.db', echo = True)
     

def creation_tables():
    '''
    Fonction permettant la création des tables dans le SQL
    '''
    
    meta = MetaData()
    vol = Table("Vol", meta, 
            Column('id_vol', String, primary_key=True), 
            Column('departureTime', String), 
            Column('arrivalTime', String),
            Column('duration', String),
            Column('departureAirportCode', String),
            Column('arrivalAirportCode', String),
            Column('airlinecodes', String),
            Column('departureDate', String),
            Column('arrivalDate', String), 
            extend_existing = True)

    price = Table("Price", meta, 
            Column('id_price', String), 
            Column('totalAmount', Float),
            Column('amountPerAdult', Float),
            Column('amountPerChild', Float),
            Column('amountPerInfant', Float),
            extend_existing = True)

    events = Table("Events", meta,
            Column('title', String),
            Column('day', String),
            Column('month', String),
            Column('city', String),
            extend_existing = True)

    airport = Table("Airport", meta,
            Column('airportCode', String, primary_key = True),
            Column('airportName', String),
            extend_existing = True)

    airline = Table("Airline", meta,
            Column('airlineCode', String, primary_key = True),
            Column('airlineName', String),
            extend_existing = True)
    
    meta.create_all(DB_SQL_connect())

def insertion(mdb):
    '''
    Fonction permettant d'insérer les valeurs de la DB_Mongo dans le SQL.
    '''
    db = mdb

    cursor = db.vol.find()
    cursor2 = db.price.find()
    cursor3 = db.event.find()
    cursor4 = db.airport.find()
    cursor5 = db.airline.find()

    for item in cursor:
    
        
        id_vol = item.get('id')
        departureTime = item.get('departureTime')
        arrivalTime = item.get('arrivalTime')
        duration = item.get('duration')
        departureAirportCode = item.get('departureAirportCode')
        arrivalAirportCode = item.get('arrivalAirportCode')
        airlineCodes = item.get('airlineCodes')
        departureDate = item.get('departureDate')
        arrivalDate = item.get('arrivalDate')
    
    for i in cursor2:
  
        id_price = i.get('id')
        totalAmount = i.get('totalAmount')
        amountPerAdult = i.get('amountPerAdult')
        amountPerChild = i.get('amountPerChild')
        amountPerInfant = i.get('amountPerInfant')
        
    titre = []
    jour = []
    mois = []
    ville = []
    for i in cursor3:
        titre.append(i.get('Titre'))
        jour.append(i.get('Jour'))
        mois.append(i.get('Mois'))
        ville.append(i.get('Ville'))
    
    codeNameAirport = []
    airportName = []    
    for i in cursor4:
        codeNameAirport.append(list(i.keys())[1])
        airportName.append(list(i.values())[1])
    print(codeNameAirport)
        
    codeNameAirline = []
    airlineName = []    
    for i in cursor5:
        codeNameAirline.append(list(i.keys())[1])
        airlineName.append(list(i.values())[1])    
        
    with DB_SQL_connect().connect() as connection:
        with connection.begin() as transaction:
            try:
                ##### TABLE VOL #####
                markers = ','.join('?' * 9)
                ins = 'INSERT OR REPLACE INTO vol VALUES ({markers})'
                
                ins = ins.format(markers = markers)
                
                for id_vol_it,departureTime_it,arrivalTime_it,duration_it,departureAirportCode_it,arrivalAirportCode_it,airlineCodes_it, departureDate_it, arrivalDate_it in zip(id_vol,departureTime,arrivalTime,duration,departureAirportCode,arrivalAirportCode,airlineCodes,departureDate, arrivalDate) :
                    airlineCodes_it =  ', '.join(airlineCodes_it)
                    connection.execute(ins, (id_vol_it,departureTime_it,arrivalTime_it,duration_it,departureAirportCode_it,arrivalAirportCode_it,airlineCodes_it, departureDate_it, arrivalDate_it))
                
                ##### TABLE PRICE #####
                markers = ','.join('?' * 5)
                ins = 'INSERT OR REPLACE INTO Price VALUES ({markers})'
                
                ins = ins.format(markers = markers)
                
                for id_price_it,totalAmount_it,amountPerAdult_it,amountPerChild_it,amountPerInfant_it in zip(id_price,totalAmount,amountPerAdult,amountPerChild,amountPerInfant) :
                    connection.execute(ins, (id_price_it,totalAmount_it,amountPerAdult_it,amountPerChild_it,amountPerInfant_it))
                
                ##### TABLE EVENT #####
                markers = ','.join('?' * 4)
                ins = 'INSERT OR REPLACE INTO Events VALUES ({markers})'
                
                ins = ins.format(markers = markers)
                for t, j, m, v in zip(titre, jour, mois, ville):
                    connection.execute(ins, (t, j, m, v))
                
                ##### TABLE AIRPORT #####
                markers = ','.join('?' * 2)
                ins = 'INSERT OR REPLACE INTO Airport VALUES ({markers})'
                
                ins = ins.format(markers = markers)
                
                for code,name in zip(codeNameAirport,airportName):
                    connection.execute(ins, (code, name))
                
                ##### TABLE AIRLINE #####
                markers = ','.join('?' * 2)
                ins = 'INSERT OR REPLACE INTO Airline VALUES ({markers})'
                
                ins = ins.format(markers = markers)
                
                for code,name in zip(codeNameAirline,airlineName):
                    connection.execute(ins, (code,name))
            except:
                transaction.rollback()
                raise
            else:
                transaction.commit()
                
                

def table_association(cursor):
    '''
    Fonction renvoyant la table d'association des différents tableaux du SQL
    '''
    result = cursor.execute("\
        SELECT\
            vol.id_vol,\
            vol.departureDate,\
            vol.departureTime,\
            vol.departureAirportCode,\
            air1.airportName AS Aeroport_dep,\
            vol.arrivalDate,\
            vol.arrivalTime,\
            vol.arrivalAirportCode,\
            air2.airportName AS Aeroport_arr,\
            vol.duration,\
            price.totalAmount,\
            price.amountPerAdult,\
            price.amountPerChild,\
            price.amountPerInfant\
        FROM\
            vol INNER JOIN airport air1 ON vol.departureAirportCode = air1.airportCode\
            INNER JOIN airport air2 ON vol.departureAirportCode = air2.airportCode\
            INNER JOIN price ON vol.id_vol = price.id_price\
        ")
    
    return result.fetchall()



with DB_SQL_connect().connect() as connection:
        results = connection.execute("SELECT * FROM vol")
        print(table_association(connection))
