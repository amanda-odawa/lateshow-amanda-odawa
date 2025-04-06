from random import choice as rc
from app import app
from models import db, Episode, Guest, Appearance

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        Appearance.query.delete()
        Guest.query.delete()
        Episode.query.delete()

        print("Seeding episodes...")
        episodes = [
            Episode(date = '2025-04-01', number = 1),
            Episode(date = '2025-04-02', number = 2),
            Episode(date = '2025-04-03', number = 3),
            Episode(date = '2025-04-04', number = 4),
            Episode(date = '2025-04-05', number = 5),
        ]
        db.session.add_all(episodes)

        print("Seeding guests...")
        guests = [
            Guest(name = 'Chris Hemsworth', occupation = 'Actor'),
            Guest(name = 'Emma Stone', occupation = 'Actress'),
            Guest(name = 'Neil deGrasse Tyson', occupation = 'Astrophysicist'),
            Guest(name = 'Oprah Winfrey', occupation = 'TV Host'),
            Guest(name = 'Meryl Streep', occupation = 'Actress'),
            Guest(name = 'Tom Hanks', occupation = 'Actor'),
            Guest(name = 'Ryan Reynolds', occupation = 'Actor'),
            Guest(name = 'Taylor Swift', occupation = 'Singer'),
            Guest(name = 'Kevin Hart', occupation = 'Comedian'),
            Guest(name = 'Billie Eilish', occupation = 'Singer'),
        ]
        db.session.add_all(guests)
        db.session.commit() 

        print("Adding appearances...")
        ratings = [1, 2, 3, 4, 5]
        appearances = []

        for episode in episodes:
            guest = guests.pop()  
            rating = rc(ratings)  
            appearances.append(
                Appearance(rating = rating, guest_id = guest.id, episode_id = episode.id)
            )

        db.session.add_all(appearances)
        db.session.commit()

        print("Done seeding!")
