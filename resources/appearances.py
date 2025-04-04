from flask import request
from flask_restful import Resource
from models import db, Appearance, Guest, Episode

class AppearanceResource(Resource):
    def post(self):
        data = request.get_json()
        rating = data.get('rating')
        guest_id = data.get('guest_id')
        episode_id = data.get('episode_id')

        if not rating or not guest_id or not episode_id:
            return {'errors':'rating, guest_id, and episode_id are required'}, 400
        
        guest = Guest.query.get(guest_id)
        episode = Episode.query.get(episode_id)

        if not guest or not episode:
            return {'errors':'Episode or guest not found'}, 404
        
        new_appearance = Appearance(
            rating=rating,
            guest_id=guest_id,
            episode_id=episode_id
        )

        db.session.add(new_appearance)
        db.session.commit()

        return new_appearance.to_dict_nested(), 201