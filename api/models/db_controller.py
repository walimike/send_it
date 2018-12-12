"""
This module establishes connection with DataBase
"""
from urllib.parse import urlparse
import psycopg2
import psycopg2.extras as walimike
from api import app
from api.models.models import User

class Dbcontroller:
    """
    class handles database connection
    """

    def __init__(self):
        database_url = app.config['DATABASE_URL']
        parsed_url = urlparse(database_url)
        dbname = parsed_url.path[1:]
        user = parsed_url.username
        host = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port
        self.conn = psycopg2.connect(
            database=dbname,
            user=user,
            password=password,
            host=host,
            port=port)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor(cursor_factory=walimike.RealDictCursor)
        print("Successfully connected to"+database_url)
        self.drop_tables()
        self.create_tables()
        admin_user = User('adminuser','admin@gmail.com','1234567890','admin')
        if not self.fetch_user(admin_user):
            self.add_user(admin_user)


    def create_tables(self):
        """
        method creates tables
        """
        user_table = "CREATE TABLE IF NOT EXISTS users(usrId serial PRIMARY KEY,\
          username varchar(50), email varchar(100), password varchar(20),\
          role varchar(15))"

        parcels_table = "CREATE TABLE IF NOT EXISTS parcels(parcelId serial PRIMARY KEY,\
          parcel_name varchar(100), price integer, parcel_status varchar(20),\
          usrId INTEGER REFERENCES users(usrId), parcel_source varchar(40),\
          parcel_destination varchar(40), present_location varchar(40), parcel_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP)"
          #FOREIGN KEY (user_id) REFERENCES users(user_id) )""",

        self.cursor.execute(user_table)
        self.cursor.execute(parcels_table)

    def drop_tables(self):
        """
        method drops tables
        """
        drop_user_table = "DROP TABLE users cascade"
        drop_parcel_table = "DROP TABLE parcels cascade"
        self.cursor.execute(drop_user_table)
        self.cursor.execute(drop_parcel_table)

    def fetch_all_entries(self,table_name):
        """ Fetches all entries from the database"""
        query = ("SELECT * FROM %s;") %(table_name)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows
        
    def add_user(self,new_user):
        self.cursor.execute("INSERT INTO users(username,email,password,role) VALUES\
        (%s, %s, %s, %s);",(new_user.name,new_user.email,new_user.password,new_user.role))

    def fetch_user(self,user):
        """Returns a user in form of a dict or None if user not found"""
        query = "SELECT * FROM users WHERE username=%s"
        self.cursor.execute(query, (user.name,))
        user = self.cursor.fetchone()
        return user

    def fetch_all_users(self):
        return self.fetch_all_entries('users')

    def add_parcel(self,parcel):
        self.cursor.execute("INSERT INTO parcels(parcel_name,price,\
        parcel_status,usrId,parcel_source,parcel_destination,present_location)\
        VALUES(%s, %s, %s, %s, %s, %s, %s);",(parcel.name,parcel.price,\
        parcel.status,parcel.id,parcel.source,parcel.destination,parcel.location))

    def fetch_all_orders(self):
        return self.fetch_all_entries('parcels')

    def fetch_parcel(self,column,did):
        """Returns a user in form of a dict or None if user not found"""
        query = """SELECT * FROM parcels WHERE {0}={1}""".format(column,did,)
        self.cursor.execute(query,)
        parcel = self.cursor.fetchall()
        return parcel

    def fetch_specific_user(self,did):
        """Returns a user in form of a dict or None if user not found"""
        query = """SELECT * FROM users WHERE usrid={0}""".format(did,)
        self.cursor.execute(query,)
        parcel = self.cursor.fetchone()
        return parcel

    def update_parcel(self,column,value, parcel_id):
            query = """UPDATE parcels SET {0} = '{1}' WHERE parcelid  = {2}""".format(column,value, parcel_id)
            self.cursor.execute(query,)

    def query_last_item(self):
        query = """SELECT * FROM parcels ORDER BY parcelid DESC LIMIT 1"""
        self.cursor.execute(query,)
        parcel = self.cursor.fetchone()
        return parcel
