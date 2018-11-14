
class User:
    """
    Creates a user object for each parcel owner.
    """
    def __init__(self,name,id):
        self.name = name
        self.id = id


class Parcel:
    """
    Creates a parcel object for each order recieved.
    """
    def __init__(self,parcel,source,destination,id):
        self.parcel = parcel
        self.source = source
        self.destination = destination
        self.parcelid = id
        self.status = "In Transit"
