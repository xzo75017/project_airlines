from sqlalchemy import create_engine, MetaData
from sql_database import table_association

def dash_handler(donnee):
    engine = create_engine('sqlite:///travel.db', echo = True)

    meta = MetaData()

    with engine.connect() as connection:
        results = connection.execute("SELECT * FROM vol")
        return results.fetchall()