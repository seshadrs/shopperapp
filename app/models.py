from app import db
from datetime import datetime
import constants


class Applicant(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), index=True, unique=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    phone = db.Column(db.String(10), unique=True)
    zipcode = db.Column(db.String(5), index=True)
    created_time = db.Column(db.DateTime, index=True)
    answers = db.Column(db.String())
    events = db.relationship('Event', backref='author', lazy='dynamic')

    def __init__(self,email,firstname,lastname,phone,zipcode):
        """ Creates an Applicant object initialized with the supplied values. """
        
        self.validate_email(email)
        self.validate_firstname(firstname)
        self.validate_lastname(lastname)
        self.validate_phone(phone)
        self.validate_zipcode(zipcode)
        
        self.email=email
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        self.zipcode=zipcode
        self.created_time= datetime.utcnow()

    def __repr__(self):
        """ Returns a string representation of the Applicant object with the firstname, lastname, email, phone and zipcode fields """
        return '<Applicant %r %r %r %r %r>' % (self.firstname,self.lastname,self.email,self.phone,self.zipcode)

    def commit(self):
        """ Commits this Applicant object to the sqlite DB """
        db.session.add(self)
        db.session.commit()

    def validate_email(self,email):
        # TODO : implement. check for any sql injection
        if not True:
            raise ValueError('Invalid email')

    def validate_firstname(self,firstname):
        # TODO : implement. check for any sql injection
        if not True:
            raise ValueError('Invalid firstname')

    def validate_lastname(self,lastname):
        # TODO : implement. check for any sql injection
        if not True:
            raise ValueError('Invalid lastname')

    def validate_phone(self,phone):
        # TODO : implement. check for any sql injection
        if not True:
            raise ValueError('Invalid phone')

    def validate_zipcode(self,zipcode):
        # TODO : implement. check for any sql injection
        if not True:
            raise ValueError('Invalid zipcode')



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'),index=True)
    event_type = db.Column(db.String())        # TODO: make event_type an enum
    created_time = db.Column(db.DateTime, index=True)

    def __init__(self,applicant_id,event_type):
        """ Creates an Event object initialized with the supplied values. applicant_id can take the value None """
        self.applicant_id=applicant_id
        self.event_type=event_type
        self.created_time= datetime.utcnow()

    def __repr__(self):
        """ Returns a string representation of the Event object with the applicant_id, event_type """
        return '<Event %r %r>' % (self.applicant_id, self.event_type)

    def commit(self):
        """ Commits this Event object to the sqlite DB """
        db.session.add(self)
        db.session.commit()


