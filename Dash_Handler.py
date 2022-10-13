from sqlalchemy import create_engine, MetaData
from sql_database import table_association

def dash_handler(donnee):
    engine = create_engine('sqlite:///travel.db', echo = True)

    meta = MetaData()

    with engine.connect() as connection:
        return table_association(connection)