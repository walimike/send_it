from api.models.models import Parcel, User
from api.models.db_controller import Dbcontroller

class ParcelDb(Dbcontroller):

    def __init__(self,database_url):
        super().__init__(database_url)

    def add_parcel(self,new_parcel):
        self.cursor.execute("INSERT INTO parcels(parcel_name,price,\
        parcel_status,usrId) VALUES(%s, %s, %s, %s);",\
        (new_parcel.name,new_parcel.price,new_parcel.status,new_parcel.id))
