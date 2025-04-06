from flask_restful import Resource
from models import Episode

class EpisodesListResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [episode.to_dict() for episode in episodes], 200
    
class EpisodeResource(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if episode:
            return episode.to_dict_with_appearances(), 200
        return {'error':'Episode not found'}, 404

