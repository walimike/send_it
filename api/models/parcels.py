
class ParcelList:
    """
    Class containing a list of all parcel orders and the various users.
    """
    def __init__(self):
        self.parcel_list = []
        self.user_list = []

    def fetch_all_orders(self):
        return self.parcel_list

my_parcels = ParcelList()

print(my_parcels.parcel_list)
