from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from models import db
from resources.episodes import EpisodesListResource, EpisodeResource
from resources.guests import GuestsListResource
from resources.appearances import AppearanceResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# Routes
api.add_resource(EpisodesListResource, '/episodes')
api.add_resource(EpisodeResource, '/episodes/<int:id>')
api.add_resource(GuestsListResource, '/guests')
api.add_resource(AppearanceResource, '/appearances')

if __name__ == '__main__':
    app.run(debug = True, port = 5555)
