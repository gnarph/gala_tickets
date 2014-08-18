from google.appengine.ext import db

class Seat(object):
    """
    A seat
    """
    name = db.StringProperty()
    position_x = db.IntegerProperty()
    position_y = db.IntegerProperty()

class Patron(object):
    """
    A person
    """
    name = db.StringProperty()
    email = db.StringProperty()
    phone = db.StringProperty()
    member = db.BooleanProperty()

class PatronSeat(object):
    """
    Seat that a person has
    """
    seat = db.ReferenceProperty(Seat)
    patron = db.ReferenceProperty(Patron)
    start = db.DateProperty()
    end = db.DateProperty()
