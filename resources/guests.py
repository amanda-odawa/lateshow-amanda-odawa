from flask_restful import Resource
from models import Guest

class GuestsListResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return [guest.to_dict() for guest in guests], 200