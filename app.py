import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movie, Actor, db
from auth.auth import AuthError, requires_auth

RECORDS_PER_PAGE = 10


def paginate_records(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page-1) * RECORDS_PER_PAGE
    end = start + RECORDS_PER_PAGE

    records = [record.format() for record in selection]
    current_records = records[start: end]

    return current_records


def create_app():
    # creating & configuring the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
      return response  
    
    @app.route('/')
    def index():
        return 'Welcome to Casting Agency BackEnd app'


    # get actors
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors():
        selection = Actor.query.order_by(Actor.id).all()
        current_actors = paginate_records(request, selection)

        if current_actors == []:
            abort(404)

        return jsonify({
            'success': True,
            'actors': current_actors,
            'total_actors': len(selection)
        })

    # get movies
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies():
        selection = Movie.query.order_by(Movie.id).all()
        current_movies = paginate_records(request, selection)

        if current_movies == []:
            abort(404)

        return jsonify({
            'success': True,
            'movies': current_movies,
            'total_movies': len(selection)
        })

    # delete an actor
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(actor_id):

        try:
            actor = Actor.query.get(actor_id)
            actor.delete()
            return jsonify({
                'success': True,
                'deleted': actor_id,
                'total_actors': len(Actor.query.all())
            })
        except:
            abort(422)

    # delete a movie
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(movie_id):

        try:
            movie = Movie.query.get(movie_id)
            movie.delete()
            return jsonify({
                'success': True,
                'deleted': movie_id,
                'total_movies': len(Movie.query.all())
            })
        except:
            abort(422)

    # add an actor
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor():
        body = request.get_json()
        try:
            name = body.get('name', None)
            age = body.get('age', None)

            actor = Actor(name=name,
                          age=age
                          )
            actor.insert()
            return jsonify({
                'success': True,
                'posted': actor.id,
                'total_actors': len(Actor.query.all())
            })

        except:
            abort(422)

    # create movie
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie():
        body = request.get_json()
        try:
            title = body.get('title', None)
            date = body.get('release_date', None)
            movie = Movie(title=title,
                          release_date=date
                          )
            movie.insert()
            return jsonify({
                'success': True,
                'posted': movie.id,
                'total_movies': len(Movie.query.all())
            })

        except:
            abort(422)

    # edit a movie
    @app.route('/movies/<movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(movie_id):

        movie = Movie.query.get(movie_id)
        # if not movie:
        #     abort(404)

        body = request.get_json()
        try:
            title = body.get('title', None)
            date = body.get('release_date', None)

            if title:
                movie.title = title

            if date:
                movie.release_date = date

            movie.update()

            return jsonify({
                'success': True,
                'id': movie_id
            }), 200

        except:
            abort(400)

    # edit an actor
    @app.route('/actors/<actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actor(actor_id):

        actor = Actor.query.get(actor_id)
        # if not actor:
        #     abort(404)

        body = request.get_json()
        try:
            name = body.get('name', None)
            age = body.get('age', None)

            if name:
                actor.name = name

            if age:
                actor.age = age

            actor.update()

            return jsonify({
                'success': True,
                'id': actor_id
            }), 200

        except:
            abort(400)

   
    # get actor's movies
    @app.route('/actor/<int:actor_id>/movies')
    @requires_auth('get:movies')
    def get_movies_from_actor(actor_id):
        actor = Actor.query.get(actor_id)


        if not actor:
            abort(404)

        movies = actor.movies    
        current_movies = paginate_records(request, movies)

        return jsonify({
            'success': True,
            'movies': current_movies,
            'current_actor': actor.name
        })

    # get movie's actors
    @app.route('/movie/<int:movie_id>/actors')
    @requires_auth('get:actors')
    def get_actors_from_movie(movie_id):
        movie = Movie.query.get(movie_id)


        if not movie:
            abort(404)

        actors = movie.actors    
        current_actors = paginate_records(request, actors)

        return jsonify({
            'success': True,
            'actors': current_actors,
            'current_movie': movie.title
        }) 


    # add association between movies & artists
    @app.route('/association', methods=['POST'])
    @requires_auth('post:associations')
    def create_association():
        
        body = request.get_json()

        try:
            actor_id = body.get("actor_id", None)
            movie_id = body.get("movie_id", None)
            
            movie = Movie.query.get(movie_id)
            actor = Actor.query.get(actor_id)
            
            actor.movies.append(movie)
            
            db.session.commit()
            
            return jsonify({
                'success': True
            })

        except:
            abort(422)    

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found!'
        }), 404

    @app.errorhandler(405)
    def not_alllowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed!'
        }), 405

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request!'
        }), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    return app
