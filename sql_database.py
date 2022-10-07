#Importer la librairie mysql connector pour la base de donnée mysql
import mysql.connector
import json 

def creation_connection(self):
    #Création d'un objet de connection pour la base de donnée 
    conn_object=mysql.connector.connect(host="localhost", port="3307", user="root", password="")
    #Création d'un curseur pour l'exécution des requêtes
    db_cursor = conn_object.cursor()
    result = db_cursor.execute("DROP DATABASE travel;")
    #Création de la base de donnée
    db_cursor.execute("CREATE DATABASE travel;")
    db_cursor.execute("USE travel;")
    #Création de la table vol 
    db_cursor.execute("CREATE TABLE vol(id_vol VARCHAR(55) PRIMARY KEY , departureTime VARCHAR(55), arrivalTime VARCHAR(55), duration VARCHAR(55), departureAirportCode VARCHAR(55), arrivalAirportCode VARCHAR(55), airlinecodes VARCHAR(55), departureDate VARCHAR(55), arrivalDate VARCHAR(55))")
    #Création de la table price
    db_cursor.execute("CREATE TABLE price(id_price VARCHAR(255) , totalAmount FLOAT, amountPerAdult FLOAT, amountPerChild FLOAT, amountPerInfant FLOAT)")
    #Création de la table event
    db_cursor.execute("CREATE TABLE eventss(title VARCHAR(55), day VARCHAR(55), month VARCHAR(55), city VARCHAR(55))")
    #Création de la table airport
    db_cursor.execute("CREATE TABLE airport(airportCode VARCHAR(55) PRIMARY KEY,airportName VARCHAR(55)) ")
    #Création de la table airline
    db_cursor.execute("CREATE TABLE airline(airlineCode VARCHAR(55) PRIMARY KEY,airlineName VARCHAR(55))")



#print(jdata2)


def table_association(cursor):
    cursor.execute("""\
        SELECT
        vol.id_vol,
        vol.departureDate,
        vol.departureTime,
        vol.departureAirportCode,
        air1.airportName AS Aeroport_dep,
        vol.arrivalDate,
        vol.arrivalTime,
        vol.arrivalAirportCode,
        air2.airportName AS Aeroport_arr,
        vol.duration,
        price.totalAmount,
        price.amountPerAdult,
        price.amountPerChild,
        price.amountPerInfant
        FROM
        vol INNER JOIN airport air1 ON vol.departureAirportCode = air1.airportCode
        INNER JOIN airport air2 ON vol.departureAirportCode = air2.airportCode
        INNER JOIN price ON vol.id_vol = price.id_price
        """)
    
    return cursor.fetchall()
# db_cursor.fetchall()

# db_cursor.execute("SELECT airlinecodes FROM vol;")
# db_cursor.fetchall()


    