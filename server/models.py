from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    birthday = db.relationship('Birthday', backref='zookeeper')


    id = db.Column(db.Integer, primary_key=True)

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    spiecies = db.relationship('Pet', backref='owner')

    def __repr__(self):
        return f'<Pet Owner {self.name}>'
