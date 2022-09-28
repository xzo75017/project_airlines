#Importer la librairie mysql connector pour la base de donnée mysql
import mysql.connector
import json 
#Création d'un objet de connection pour la base de donnée 
conn_object=mysql.connector.connect(host="localhost", port="3307", user="root", password="")

#Création d'un curseur pour l'exécution des requêtes
db_cursor = conn_object.cursor()

#Création de la base de donnée
db_cursor.execute("CREATE DATABASE Travel;")
#Création de la table vol 
db_cursor.execute("CREATE TABLE vol(id_vol INT PRIMARY KEY, departureTime TIME, arrivalTime TIME, duration TIME, departureAirportCode VARCHAR(55), arrivalAirportCode VARCHAR(55), airlinecodes VARCHAR(55))")
#Création de la table price
db_cursor.execute("CREATE TABLE price(id_price INT PRIMARY KEY, totalAmount DECIMAL, amountPerAdult DECIMAL, amountPerChild DECIMAL, amountPerInfant DECIMAL")
#Création de la table event
db_cursor.execute("CREATE TABLE eventss(id_event INT PRIMARY KEY, title VARCHAR(55), day VARCHAR(55), month VARCHAR(55), city VARCHAR(55)")
#Création de la table airport
db_cursor.execute("CREATE TABLE airport(id_airport INT PRIMARY KEY,airportName VARCHAR(55)")
#Création de la table airline
db_cursor.execute("CREATE TABLE airline(id_airline INT PRIMARY KEY,airlineName VARCHAR(55)")

#lecture + Chargement des fichiers 
jdata = [json.loads(line) for line in open('Vol_json', 'r')]
jdata2 = [json.loads(line) for line in open('price_json', 'r')]
jdata3 = [json.loads(line) for line in open('event_json',encoding='utf8')]
jdata4 = [json.loads(line) for line in open('airport_json', 'r')]

for item in jdata:
    departureTime = item.get("departureTime")
    arrivalTime = item.get("arrivalTime")
    duration = item.get("duration")
    departureAirportCode = item.get("departureAirportCode")
    arrivalAirportCode = item.get("arrivalAirportCode")
    airlineCodes = item.get("airlineCodes")
    db_cursor.execute("insert into vol(id_vol,departureTime,arrivalTime,duration,departureAirportCode,arrivalAirportCode,airlineCodes) value (%s,%s,%s,%s,%s,%s,%s)", (departureTime,arrivalTime,duration,departureAirportCode,arrivalAirportCode,airlineCodes))

    conn_object.commit()
