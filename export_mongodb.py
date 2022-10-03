import json 
import subprocess
import sys
import os
#import arrow
from multiprocessing import pool

try:
    import ujson as json
except ImportError:
    import json

#import keyring

DAYFMT = '%a_%b_%d_%Y'
SERVICE = 'mongoexport'

class MongoExport(object):

    def __init__(self, password, database ,  collection, filetype,output=None):
        """Constructor for mongoexport job.
        :param fields:  Fields as a list which will be selected for export.
                        Each field may reference a subdocument or value using
                        dot notation.
        """

        now = arrow.now()
        todaystr = now.floor('day').strftime(DAYFMT)
        filename = "%s_%s" % (collection, now.strftime('%X'))
        output = normalized_path(output)
        if not output:
            output = "%s/%s/%s/%s" % (SERVICE.lower(), collection, todaystr, filename)
        elif os.path.isdir(output):
            output = "%s/%s" % (output, filename)
        elif os.path.isfile(output):
            pass
        output = normalized_path(output)
        self.dirs, self.filename = os.path.split(output)

        ensure_dirpath(self.dirs)
        self.docspath = os.path.join(self.dirs, 'documents')
        ensure_dirpath(self.docspath)

       
        if not password:
            password = get_configured_value('password')


        self.password = password
        self.database = database
        self.collection = collection
        self.filetype = filetype
       
        self.output = output
        
        def get_command(self):
            command = ("mongoexport --uri mongodb+srv://DST-PROJECT:{password}@cluster0.7wo11db.mongodb.net/{database} --collection {collection} --type {filetype} --out {output}")
        command = command.format(password=self.password, db=self.database,collection=self.collection,output=self.output)
        
        if self.password:
            command += " --password %s" % self.password
        return command
    
        def run(self):
            command = self.get_command()
            return execute(command) 
         
        def _file_per_document(exportfile):
            if not os.path.exists(exportfile):
                print ("%s doesn't exist!" % exportfile)
            return
        dirs, _ = os.path.split(exportfile)
        docspath = os.path.join(dirs, 'documents')
        ensure_dirpath(docspath)
        expfile = open(exportfile, 'r')
        

    
        
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    con = None
    try:
       con = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return con

def create_vol(con, jdata):
    """
    Create a new project into the projects table
    :param conn:
    :param vol:
    :return: vol id
    """
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
            
    
    return cur.lastrowid


def create_price(con, jdata2):
    """
    Create a new project into the projects table
    :param conn:
    :param price:
    :return: price id
    """
    for i in jdata2:
        print(type(item))
        id_price = item.get('id')
        totalAmount = i.get('totalAmount')
        amountPerAdult = i.get('amountPerAdult')
        amountPerChild = i.get('amountPerChild')
        amountPerInfant = i.get('amountPerInfant')
    
        print(id_price)
   
        for id_price_it,totalAmount_it,amountPerAdult_it,amountPerChild_it,amountPerInfant_it in zip(id_price,totalAmount,amountPerAdult,amountPerChild,amountPerInfant) :
            cur.execute("insert into price(id_price,totalAmount,amountPerAdult,amountPerChild,amountPerInfant) values (?,?,?,?,?)" , (id_price_it,totalAmount_it,amountPerAdult_it,amountPerChild_it,amountPerInfant_it))
    return cur.lastrowid


def create_events(con, jdata3):
    """
    Create a new project into the projects table
    :param conn:
    :param events:
    :return: events id
    """
    for i in jdata3:
        titre = i.get('Titre')
        jour = i.get('Jour')
        mois = i.get('Mois')
        ville = i.get('Ville')
        cur.execute("insert into eventss (title,day,month,city) values (?,?,?,?)" , (titre,jour,mois,ville))
    
    
    return cur.lastrowid


def create_airport(con, jdata4):
    """
    Create a new project into the projects table
    :param conn:
    :param events:
    :return: events id
    """
    for i in jdata4:
        codeNameAirport = list(i.keys())[0]
        airportName = list(i.values())[0]
        print(airportName)
        cur.execute("insert into airport (airportCode, airportName) values (?, ?);" , (codeNameAirport, airportName))
    
    return cur.lastrowid


def create_airline(con, jdata5):
    """
    Create a new project into the projects table
    :param conn:
    :param events:
    :return: events id
    """
    key= '_id'

    for i in range(len(jdata5)):
        del jdata5[i][key]
    
    for i in jdata5:
        codeNameAirline = list(i.keys())[0]
        airlineName = list(i.values())[0]
        cur.execute("insert into airline (airlineCode, airlineName) values (?, ?);" , (codeNameAirline, airlineName))

    return cur.lastrowid