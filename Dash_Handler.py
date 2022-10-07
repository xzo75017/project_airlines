from sqlalchemy import create_engine, MetaData

def dash_handler(donnee):
    engine = create_engine('sqlite:///travel.db', echo = True)

    meta = MetaData()

    with engine.connect() as connection:
        results = connection.execute("SELECT * FROM vol")
        return results.fetchall()