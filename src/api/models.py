from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy.fields import Nested
import apiflask.fields as af
import apiflask.validators as av

db = SQLAlchemy()
ma = Marshmallow()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Float)
    profile_color = db.Column(db.String(8))
    pet_color = db.Column(db.Text)
    rating = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(
        db.DateTime, default=datetime.now,
        onupdate=datetime.now, nullable=True
    )


class PaginationSchema(ma.Schema):
    page = af.Integer(load_default=1)
    per_page = af.Integer(
        load_default=20, validate=av.Range(max=30)
    )


class PetOutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pet
        fields = (
            'id', 'name', 'age', 'profile_color',
            'pet_color', 'rating', 'created', 'updated'
        )


class PetsOutSchema(ma.Schema):
    pets = af.List(af.Nested('PetOutSchema'))
    pagination = af.Nested(PaginationSchema)


class PetPutSchema(ma.SQLAlchemyAutoSchema):
    id = af.Integer(required=True)
    name = af.String(required=False)
    age = af.Float(required=False, validate=av.Range(min=0))
    profile_color = af.String(required=False)
    pet_color = af.String(required=False)
    rating = af.Integer(required=False, validate=av.Range(min=10))

    class Meta:
        model = Pet
        fields = (
            'id', 'name', 'age',
            'profile_color', 'pet_color', 'rating'
        )


class PetPostSchema(ma.SQLAlchemyAutoSchema):
    name = af.String(required=False)
    age = af.Float(required=False, validate=av.Range(min=0))
    profile_color = af.String(required=False)
    pet_color = af.String(required=False)
    rating = af.Integer(required=False, validate=av.Range(min=10))

    class Meta:
        model = Pet
        fields = (
            'name', 'age', 'profile_color', 'pet_color', 'rating'
        )
