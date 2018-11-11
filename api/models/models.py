import uuid

class User:
    def __init__(self,name,id):
        self.name = name
        self.id = id


class Parcel:
    def __init__(self,parcel,source,destination,id):
        self.parcel = parcel
        self.source = source
        self.destination = destination
        self.parcelid = id
