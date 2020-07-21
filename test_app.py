import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Actor, Movie


class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "recap"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            'hos', 'zacbrand', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_movie = {"title": 'new title1',
                          "release_date": '2019-10-21 20:06:07'
                          }

        self.new_actor = {"name": 'new name1',
                          "age": 50
                          }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # tests

    def test_get_paginated_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_movies'])

    def test_404_send_requesting_beyond_valid_movie_page(self):
        res = self.client().get('/movies?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found!')

    def test_get_paginated_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_actors'])

    def test_404_send_requesting_beyond_valid_actor_page(self):
        res = self.client().get('/actors?page=2000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found!')

    def test_delete_movie(self):
        movie_id = Movie.query.filter(
            Movie.title == self.new_movie["title"]).one_or_none().id
        res = self.client().delete(f'/movies/{movie_id}')
        data = json.loads(res.data)

        movie = Movie.query.get(movie_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], movie_id)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_movies'])
        self.assertEqual(movie, None)

    def test_422_delete_movie_fail(self):
        res = self.client().delete('/movies/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_actor(self):
        actor_id = Actor.query.filter(
            Actor.name == self.new_actor["name"]).one_or_none().id
        res = self.client().delete(f'/actors/{actor_id}')
        data = json.loads(res.data)

        actor = Actor.query.get(actor_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], actor_id)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_actors'])
        self.assertEqual(actor, None)

    def test_422_delete_actor_fail(self):
        res = self.client().delete('/actors/4000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_add_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['posted'])
        self.assertTrue(data['total_movies'])

    def test_405_if_movie_addition_not_allowed(self):
        res = self.client().post('/movies/45', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed!')

    def test_add_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['posted'])
        self.assertTrue(data['total_actors'])

    def test_405_if_actor_addition_not_allowed(self):
        res = self.client().post('/actors/45', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed!')

    def test_edit_movie_title(self):
        movie_id = 2
        res = self.client().patch(f'/movies/{movie_id}', json={"title": "test"})
        data = json.loads(res.data)
        movie = Movie.query.get(movie_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie.format()['title'], "test")

    def test_400_for_failed_update_movie(self):
        res = self.client().patch('/movies/5')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'bad request!')

    def test_edit_actor_name(self):
        actor_id = 5
        res = self.client().patch(f'/actors/{actor_id}', json={"name": "hos"})
        data = json.loads(res.data)
        actor = Actor.query.get(actor_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['name'], "hos")

    def test_400_for_failed_update_actor(self):

        res = self.client().patch('/actors/5')

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'bad request!')

    def test_get_movies_by_actor(self):
        res = self.client().get('/actor/1/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['current_actor'])

    def test_404_fail_get_movies_by_actor(self):
        res = self.client().get('/actor/2000/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found!')

    def test_get_actors_by_movie(self):
        res = self.client().get('/movie/1/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['current_movie'])

    def test_404_fail_get_actors_by_movie(self):
        res = self.client().get('/movie/2000/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found!')
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
