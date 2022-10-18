from sql_database import DB_SQL_connect, creation_tables


def drop():
    with DB_SQL_connect().connect() as connection:
       connection.execute('DROP TABLE City')
       
       
drop()

creation_tables()

#Insertion dans City si il n'est pas déja présent
io = open("app/Data/SQL/database/cities.txt", "r")
lines = io.readlines()
split = []
for element in lines:
    split.append(str.split(element, "\t"))
    
with DB_SQL_connect().connect() as connection:
        with connection.begin() as transaction:
            try:
                ##### TABLE CITY #####
                markers = ','.join('?' * 2)
                ins = 'INSERT OR REPLACE INTO City VALUES ({markers})'
                
                ins = ins.format(markers = markers)
                
                for i in range (len(split)-1):
                    if(len(split[i])==3):
                        connection.execute(ins, (split[i][2].strip(),split[i][0]))
            except:
                transaction.rollback()
                raise
            else:
                transaction.commit()
                
def drop():
    with DB_SQL_connect().connect() as connection:
       connection.execute('DROP TABLE City')
        