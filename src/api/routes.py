"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from apiflask import APIBlueprint, pagination_builder
from apiflask.schemas import EmptySchema
from flask import Flask, request, jsonify, url_for, Blueprint
from flask.views import MethodView
from api.models import (
    db, User, Pet, PetPutSchema, PetOutSchema,
    PetsOutSchema, PaginationSchema, PetPostSchema
)
from api.utils import generate_sitemap, APIException

api = APIBlueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/pets')
class Pets(MethodView):
    @api.input(PaginationSchema, 'query')
    @api.output(PetsOutSchema)
    def get(self, query):
        pagination = Pet.query.paginate(
            page=query['page'],
            per_page=query['per_page']
        )
        return {
            'pets': pagination.items,
            'pagination': pagination_builder(pagination)
        }

    @api.input(PetPostSchema)
    @api.output(EmptySchema)
    def post(self, query):
        db.session.merge(Pet(**query))
        db.session.commit()

    @api.input(PetPutSchema)
    @api.output(EmptySchema)
    def put(self, query):
        pet = Pet.query.filter_by(id=query['id']).first()
        for k, v in query.items():
            if k != 'id':
                setattr(pet, k, v)
        db.session.merge(pet)
        db.session.commit()
    
    @api.input(PetPutSchema)
    @api.output(EmptySchema)
    def delete(self, query):
        Pet.query.filter_by(id=query['id']).delete()
        db.session.commit()
