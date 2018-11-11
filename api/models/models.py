import uuid

class User:
    def __init__(self,name):
        self.name = name
        self.id = int(uuid.uuid4())


class Parcel:
    def __init__(self,parcel,source,destination):
        self.parcel = parcel
        self.source = source
        self.destination = destination
        self.parcelid = int(uuid.uuid1())
