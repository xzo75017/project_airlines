from DB_Mongo import DB_Mongo
import sqlite3
from sql_database import table_association

db = DB_Mongo()

db1 = db.connexion()
db2 = db1.test
collection = db2["Vol"]  
cursor = collection.find()

con = sqlite3.connect("travel.db")
cur = con.cursor()

cur.execute("DROP TABLE vol;")
cur.execute("DROP TABLE price;")
cur.execute("DROP TABLE eventss;")
cur.execute("DROP TABLE airport;")
cur.execute("DROP TABLE airline;")

cur.execute("CREATE TABLE vol(id_vol VARCHAR(55) PRIMARY KEY , departureTime VARCHAR(55), arrivalTime VARCHAR(55), duration VARCHAR(55), departureAirportCode VARCHAR(55), arrivalAirportCode VARCHAR(55), airlinecodes VARCHAR(55), departureDate VARCHAR(55), arrivalDate VARCHAR(55))")
#Création de la table price
#db_cursor.execute("CREATE TABLE price(id_price VARCHAR(255) , totalAmount FLOAT, amountPerAdult FLOAT, amountPerChild FLOAT, amountPerInfant FLOAT)")
cur.execute("CREATE TABLE price(id_price VARCHAR(255) , totalAmount FLOAT, amountPerAdult FLOAT, amountPerChild FLOAT, amountPerInfant FLOAT)")
#Création de la table event
#db_cursor.execute("CREATE TABLE eventss(title VARCHAR(55), day VARCHAR(55), month VARCHAR(55), city VARCHAR(55))")
cur.execute("CREATE TABLE eventss(title VARCHAR(55), day VARCHAR(55), month VARCHAR(255), city VARCHAR(55))")
#Création de la table airport
#db_cursor.execute("CREATE TABLE airport(airportCode VARCHAR(55) PRIMARY KEY,airportName VARCHAR(55)) ")
cur.execute("CREATE TABLE airport(airportCode VARCHAR(55) PRIMARY KEY,airportName VARCHAR(55)) ")
#Création de la table airline
#db_cursor.execute("CREATE TABLE airline(airlineCode VARCHAR(55) PRIMARY KEY,airlineName VARCHAR(55))")
cur.execute("CREATE TABLE airline(airlineCode VARCHAR(55) PRIMARY KEY,airlineName VARCHAR(55))")

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
    for id_vol_it,departureTime_it,arrivalTime_it,duration_it,departureAirportCode_it,arrivalAirportCode_it,airlineCodes_it, departureDate_it, arrivalDate_it in zip(id_vol,departureTime,arrivalTime,duration,departureAirportCode,arrivalAirportCode,airlineCodes,departureDate, arrivalDate) :
        airlineCodes_it =  ', '.join(airlineCodes_it)
        cur.execute("insert into vol(id_vol,departureTime,arrivalTime,duration,departureAirportCode,arrivalAirportCode,airlineCodes,departureDate, arrivalDate) values (?,?,?,?,?,?,?,?,?) ON CONFLICT (id_vol) DO UPDATE SET id_vol = ?;", (id_vol_it,departureTime_it,arrivalTime_it,duration_it,departureAirportCode_it,arrivalAirportCode_it,airlineCodes_it,departureDate_it, arrivalDate_it, id_vol_it))
        
collection2 = db2["Price"]  
cursor2 = collection2.find()
   
for i in cursor2:
  
    id_price = i.get('id')
    totalAmount = i.get('totalAmount')
    amountPerAdult = i.get('amountPerAdult')
    amountPerChild = i.get('amountPerChild')
    amountPerInfant = i.get('amountPerInfant')
    
    for id_price_it,totalAmount_it,amountPerAdult_it,amountPerChild_it,amountPerInfant_it in zip(id_price,totalAmount,amountPerAdult,amountPerChild,amountPerInfant) :
        cur.execute("insert into price(id_price,totalAmount,amountPerAdult,amountPerChild,amountPerInfant) values (?,?,?,?,?)" , (id_price_it,totalAmount_it,amountPerAdult_it,amountPerChild_it,amountPerInfant_it))
        
        con.commit()


collection3 = db2["Event"]  
cursor3 = collection3.find()
   
for i in cursor3:
    titre = i.get('Titre')
    jour = i.get('Jour')
    mois = i.get('Mois')
    ville = i.get('Ville')
    cur.execute("insert into eventss (title,day,month,city) values (?,?,?,?)" , (titre,jour,mois,ville))
    
collection4 = db2["Airport"]  
cursor4 = collection4.find()

 
for i in cursor4:
    codeNameAirport = list(i.keys())[1]
    airportName = list(i.values())[1]
   
    cur.execute("insert into airport (airportCode, airportName) values (?, ?);" , (codeNameAirport, airportName))
    
collection5 = db2["Airline"]  
cursor5 = collection4.find()


    
for i in cursor5:
    codeNameAirline = list(i.keys())[1]
    airlineName = list(i.values())[1]
    cur.execute("insert into airline (airlineCode, airlineName) values (?, ?);" , (codeNameAirline, airlineName))

cur.execute("SELECT * FROM airport LIMIT 20;")

print(table_association(cur))

