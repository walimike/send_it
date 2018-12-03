class Parcel:
    """
    Creates a parcel model.
    """
    def __init__(self,name,price,usrid,source,destination):
        self.name=name
        self.price=price
        self.id=usrid
        self.source = source
        self.location = 'Unknown'
        self.destination = destination
        self.status = 'In Transit'

class User:
    """
    class creates a user model.
    """
    def __init__(self,name,email,password,role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
