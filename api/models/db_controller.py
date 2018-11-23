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
        self.create_tables()
        admin_user = User('adminuser','admin@gmail.com','@H@nN@H92','admin')
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
          parcel_destination varchar(40), present_location varchar(40))"
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
        try:
            query = ("SELECT * FROM %s;") %(table_name)
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError)as Error:
            raise Error

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

    def fetch_parcel(self,id):
        """Returns a user in form of a dict or None if user not found"""
        query = "SELECT * FROM parcels WHERE parcelid=%s"
        self.cursor.execute(query, (id,))
        parcel = self.cursor.fetchone()
        return parcel

    def fetch_parcel_by_specific(self,id):
        """Returns a user in form of a dict or None if user not found"""
        query = "SELECT * FROM parcels WHERE usrid=%s"
        self.cursor.execute(query, (id,))
        parcels = self.cursor.fetchall()
        return parcels

    def update_parcel(self,column,value, parcel_id):
            if column == 'parcel_destination':
                query = "UPDATE parcels SET parcel_destination = '{}' WHERE parcelid  = '{}'".format(value, parcel_id)
            elif column == 'parcel_status':
                query = "UPDATE parcels SET parcel_status = '{}' WHERE parcelid  = '{}'".format(value, parcel_id)
            elif column == 'present_location':
                query = "UPDATE parcels SET present_location = '{}' WHERE parcelid  = '{}'".format(value, parcel_id)
            self.cursor.execute(query,)
