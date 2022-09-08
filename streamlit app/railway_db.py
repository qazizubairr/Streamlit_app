
import psycopg2
import psycopg2.extras
from config import config


def connect():
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        
        conn = psycopg2.connect(**params)
		
        print("connected")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# def execute (connection , data):
#     cur = connection.cursor() 
#     postgres_insert_query = """ INSERT INTO bnb_houses (homes,address,rooms,dates,rent) VALUES (%s,%s,%s,%s,%s)"""
#     cur.execute(postgres_insert_query, data)
#     connection.commit()
    

def run_query(connection,query):
    cur = connection.cursor()
    cur.execute(query)
    return cur.fetchall()



    




