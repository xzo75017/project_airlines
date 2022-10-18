from sqlalchemy import Table, create_engine, MetaData, String, Column, Float
from datetime import datetime as dt


def DB_SQL_connect():
    return create_engine('sqlite:///app/Data/SQL/database/travel.db', echo = True)
     

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
            Column('Last_Scrap', String),
            extend_existing = True)

    airport = Table("Airport", meta,
            Column('airportCode', String, primary_key = True),
            Column('airportName', String),
            extend_existing = True)

    airline = Table("Airline", meta,
            Column('airlineCode', String, primary_key = True),
            Column('airlineName', String),
            extend_existing = True)
    
    city = Table("City", meta,
            Column('cityCode', String, primary_key = True),
            Column('cityName', String),
            extend_existing = True)
    
    meta.create_all(DB_SQL_connect())

def insertion_vol(mdb, count_vol, count_price):
    '''
    Fonction permettant d'insérer les valeurs de la DB_Mongo dans le SQL.
    '''
    db = mdb

    cursor = db.vol.find().limit(count_vol)
    cursor2 = db.price.find().limit(count_price)
    cursor3 = db.airport.find()
    cursor4 = db.airline.find()
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
    
    codeNameAirport = []
    airportName = []    
    for i in cursor3:
        codeNameAirport.append(list(i.keys())[1])
        airportName.append(list(i.values())[1])
    print(codeNameAirport)
        
    codeNameAirline = []
    airlineName = []    
    for i in cursor4:
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
                
def insertion_event(mdb):
    '''
    Fonction permettant d'insérer les valeurs de la DB_Mongo dans le SQL.
    '''
    
    cursor = mdb.event.find()
    
    titre = []
    jour = []
    mois = []
    ville = []
    last = []
    for i in cursor:
        titre.append(i.get('Titre'))
        jour.append(i.get('Jour'))
        mois.append(i.get('Mois'))
        ville.append(i.get('Ville'))
        last.append(i.get('Last_Scrap'))
        
    with DB_SQL_connect().connect() as connection:
        with connection.begin() as transaction:
            try:
                #On drop les valeurs existantes dans le SQL pour cette ville
                ins = 'DELETE FROM Events WHERE Events.city = (?)'
                connection.execute(ins, ville[0])
                
                #On ajoute ensuite les nouvelles valeurs
                markers = ','.join('?' * 4)
                ins = 'INSERT OR REPLACE INTO Events VALUES ({markers})'
                
                ins = ins.format(markers = markers)
                for t, j, m, v, l in zip(titre, jour, mois, ville, last):
                    connection.execute(ins, (t, j, m, v, l))
            except:
                transaction.rollback()
                raise
            else:
                transaction.commit()
                    

def table_association(cursor, depart, arrivee, start_date):
    '''
    Fonction renvoyant la table d'association des différents tableaux du SQL
    '''
    marker1 = depart + "%"
    marker2 = arrivee + "%"
    
    result = cursor.execute("""
        SELECT
            vol.id_vol,
            vol.departureDate,
            vol.departureTime,
            vol.departureAirportCode,
            ct1.cityName AS Ville_dep,
            air1.airportName AS Aeroport_dep,   
            vol.arrivalDate,
            vol.arrivalTime,
            vol.arrivalAirportCode,
            ct2.cityName AS Ville_arr,   
            air2.airportName AS Aeroport_arr,
            vol.duration,
            price.totalAmount,
            price.amountPerAdult,
            price.amountPerChild,
            price.amountPerInfant
        FROM
            vol INNER JOIN airport air1 ON vol.departureAirportCode = air1.airportCode
            INNER JOIN airport air2 ON vol.arrivalAirportCode = air2.airportCode
            INNER JOIN price ON vol.id_vol = price.id_price
            INNER JOIN city ct1 ON vol.departureAirportCode = ct1.cityCode
            INNER JOIN city ct2 ON vol.arrivalAirportCode = ct2.cityCode
        WHERE
            ct1.cityName LIKE (?) AND ct2.cityName LIKE (?) AND vol.departureDate = (?)
        """, (marker1, marker2, start_date))
    
    return result.fetchall()
