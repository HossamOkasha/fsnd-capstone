import os
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import json

database_name = "recap"
database_path = "postgresql://{}:{}@{}/{}".format(
    'hos', 'zacbrand', 'localhost:5432',
    database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


# many to many relationship

# joining table
movies_actors = db.Table(
    'association',
    db.Column('actor_id', db.Integer(), db.ForeignKey('actors.id'),
              primary_key=True),
    db.Column('movie_id', db.Integer(), db.ForeignKey('movies.id'),
              primary_key=True)
)


# parent model
class Actor(db.Model):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    movies = db.relationship('Movie', secondary=movies_actors,
                             backref='actors')

    # add 
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # edit
    def update(self):
        db.session.commit()

    # remove
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # convert to dictionary
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

    # debug method
    def __repr__(self):
        return f'<actor ID: {self.id}, name: {self.name}>'


# children model
class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(db.DateTime, nullable=False)

    # add
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # edit
    def update(self):
        db.session.commit()

    # delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # convert to dictionary
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    # debug 
    def __repr__(self):
        return f'<movie ID: {self.id}, title: {self.title}>'

