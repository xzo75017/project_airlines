from sql_database import table_association
import sqlite3

def dash_handler(donnee):
    con = sqlite3.connect("travel.db")
    cur = con.cursor()
    return table_association(cur)