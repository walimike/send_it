from api.models.models import Parcel,User

class ParcelList:
    """
    Class containing a list of all parcel orders and the various users.
    """
    def __init__(self):
        self.parcel_list = []
        self.user_list = []

    def fetch_all_orders(self):
        return self.parcel_list

    def authenticate_user_identity(self,name):
        specific_user = [user for user in self.user_list if user.name==name]
        try:
            return specific_user[0].id
        except IndexError:
            new_user = User(name,self.user_id_generator())
            self.user_list.append(new_user)
            return new_user.id

    def add_parcel(self,user_name,parcel):
        current_id = self.authenticate_user_identity(user_name)
        new_parcel = parcel.__dict__
        new_parcel['User Id'] = current_id
        self.parcel_list.append(new_parcel)

    def fetch_all_users(self):
        return [users.__dict__ for users in self.user_list]

    def parcel_id_generator(self):
        if len(self.parcel_list) == 0:
            return 1
        return self.parcel_list[-1]["parcelid"]+1

    def user_id_generator(self):
        if len(self.user_list) == 0:
            return 1
        return self.user_list[0].id+1

    def fetch_specific_order(self,id):
        specific_order = [order for order in self.parcel_list if\
         order['parcelid']==id]
        try:
            return specific_order[0]
        except IndexError:
            return

    def fetch_all_orders_by_specific_user(self,id):
        all_orders = [orders for orders in self.parcel_list if\
        orders['User Id']==id]
        return all_orders
"""
parcels=ParcelList()
new_parcel = Parcel('parcel','source','destination',1)
parcels.add_parcel('wali',new_parcel)
print(parcels.fetch_specific_order(10))
"""
