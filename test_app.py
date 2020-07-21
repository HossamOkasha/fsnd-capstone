import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
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

        # Roles
        casting_director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk1UktCWlhaRnpranphaElrLWlnZCJ9.eyJpc3MiOiJodHRwczovL2hvcy1jYXN0aW5nLWFnZW5jeS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxNzRjYTYyYWQzMmMwMDEzNTAxNTA4IiwiYXVkIjoiQWdlbmN5IiwiaWF0IjoxNTk1MzcwNjU1LCJleHAiOjE1OTU0NTcwNTUsImF6cCI6IlM0STJ6emx5U3ZXd3BvcEJCMTZpbktDRWFwMndQUjVKIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.YEb578kyZrctRbujATv57izuiIyTN1DXZN8bJL05YhjDx5uEV7X4f3CpBSTAvvs7CwwWD58_5bogWh6P3Die_z7pGUkWnIxzWsYTHeLLD0WNU5AoczgRg93OgPzuidaoFYoUmkeJ66u8-f_o-hNe1HAHI9zHB3ao7yPKzibkYdGC3Jfwv7QYH7mZpMFQaIa88SBJVLmNWh5ujiSWRXKWJmeb8ynIjsBE4N8oo5niX6OkkqIaolj1qtbyFGKvgbJ3n3yPnQ7QN2vT7_EieLAWkYYMrme7PTbWAtN1_06F0g6QzcjxL5nRB3gC-vaFX6omZxztkM9NzmtBhkT6tn4sqg'
        casting_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk1UktCWlhaRnpranphaElrLWlnZCJ9.eyJpc3MiOiJodHRwczovL2hvcy1jYXN0aW5nLWFnZW5jeS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxNzRjYzhkYmY2ZmYwMDEzNWNhMTFiIiwiYXVkIjoiQWdlbmN5IiwiaWF0IjoxNTk1MzcxMDAwLCJleHAiOjE1OTU0NTc0MDAsImF6cCI6IlM0STJ6emx5U3ZXd3BvcEJCMTZpbktDRWFwMndQUjVKIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.CTt3bzlrohc1FNN4uj1MPZnFqdfPLuekxFTgg3LtL1n5mGPSZ2OhIxEU-hdL4pHOsaRyW6nqnSNKAL9GkSdlj2hNlZFg1F8rJaALuoUbXDe71r-wUV1-0ZsCC2quVHwwdgd0taUYPiOVAKobipflotsJ3yKhV7gsOIhvWHTCbTFdMm2FtojlF4W2U1LoczV0GvWQZS_ikHw_QQqwzDW6c1V_6ryi4wYD9Z96qLgbBlOFZECLQFn5fBie4qNXArGMFbVcSuzZ7Fn3xMi7V9xlPrez5GNwzCMCp_wQgmrQ_f_UTrCxfjpmhgJbGHRmeDL4vpjFrcxMz92ldsfglBYBwg'
        executive_producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk1UktCWlhaRnpranphaElrLWlnZCJ9.eyJpc3MiOiJodHRwczovL2hvcy1jYXN0aW5nLWFnZW5jeS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ4Nzg3MzgwODkwODk1ODA0NTIiLCJhdWQiOlsiQWdlbmN5IiwiaHR0cHM6Ly9ob3MtY2FzdGluZy1hZ2VuY3kudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5NTM3MTEzMCwiZXhwIjoxNTk1NDU3NTMwLCJhenAiOiJTNEkyenpseVN2V3dwb3BCQjE2aW5LQ0VhcDJ3UFI1SiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0OmFzc29jaWF0aW9ucyIsInBvc3Q6bW92aWVzIl19.XETQyRM1ZzjIEnFqo4bswXv2mOJpXUUgWLQkJncR8kEVnOWOENTjl6_-WIWBl8y7d3GcjOQVgyUd-xD20rOOyhqe6YPLxvZeBW-PxU25rCwPQ4t5IBExz4Ggn0DQF9w3r0YJ-Cqm0-rqVIz5fTP-IvBWdiKMwpOZyMrCKRc0WxzvlHk6nAK6SGLUIO9M9P0fhZQGDM6AzpSOPUfiqRjlu6TR5kXXQ0DhpXhMx5ur_tJddpVjaLzmabs8JBdtSKGnVklguurq9K8b5YuzWJDgD9h7ot3pLdD6sC-Nw9_ezyI3bMAHEmvtYf4Mgz4J-_Rdl6Lap7I2oOMaBSlp27a-1w'
        
        self.h_casting_director = {

            'Content-type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Authorization': f'Bearer {casting_director}'

        }
        self.h_casting_assistant = {

            'Content-type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Authorization': f'Bearer {casting_assistant}'
            
        }
        self.h_executive_producer = {

            'Content-type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Authorization': f'Bearer {executive_producer}'
            
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
        res = self.client().get('/movies', headers=self.h_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_movies'])

    def test_404_send_requesting_beyond_valid_movie_page(self):
        res = self.client().get('/movies?page=1000', headers=self.h_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found!')

    def test_get_paginated_actors(self):
        res = self.client().get('/actors', headers=self.h_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_actors'])

    def test_404_send_requesting_beyond_valid_actor_page(self):
        res = self.client().get('/actors?page=2000', headers=self.h_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found!')

    def test_delete_movie(self):
        movie_id = Movie.query.filter(
            Movie.title == self.new_movie["title"]).one_or_none().id

        res = self.client().delete(f'/movies/{movie_id}', headers=self.h_executive_producer)
        data = json.loads(res.data)

        movie = Movie.query.get(movie_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], movie_id)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_movies'])
        self.assertEqual(movie, None)

    def test_422_delete_movie_fail(self):
        res = self.client().delete('/movies/1000', headers=self.h_executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_actor(self):
        actor_id = Actor.query.filter(
            Actor.name == self.new_actor["name"]).one_or_none().id
       
        res = self.client().delete(f'/actors/{actor_id}', headers=self.h_casting_director)
        data = json.loads(res.data)

        actor = Actor.query.get(actor_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], actor_id)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_actors'])
        self.assertEqual(actor, None)

    def test_422_delete_actor_fail(self):
        res = self.client().delete('/actors/4000', headers=self.h_casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_add_new_movie(self):
        res = self.client().post('/movies', headers=self.h_executive_producer, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['posted'])
        self.assertTrue(data['total_movies'])

    def test_405_if_movie_addition_not_allowed(self):
        res = self.client().post('/movies/45', headers=self.h_executive_producer, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed!')

    def test_add_new_actor(self):
        res = self.client().post('/actors', headers=self.h_casting_director, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['posted'])
        self.assertTrue(data['total_actors'])

    def test_405_if_actor_addition_not_allowed(self):
        res = self.client().post('/actors/45', headers=self.h_casting_director, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed!')

    def test_edit_movie_title(self):
        movie_id = 2
        res = self.client().patch(
            f'/movies/{movie_id}', headers=self.h_casting_director, json={"title": "test"})
        data = json.loads(res.data)
        movie = Movie.query.get(movie_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie.format()['title'], "test")

    def test_400_for_failed_update_movie(self):
        res = self.client().patch('/movies/5', headers=self.h_casting_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'bad request!')

    def test_edit_actor_name(self):
        actor_id = 5
        res = self.client().patch(f'/actors/{actor_id}', headers=self.h_casting_director, json={"name": "hos"})
        data = json.loads(res.data)
        actor = Actor.query.get(actor_id)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['name'], "hos")

    def test_400_for_failed_update_actor(self):

        res = self.client().patch('/actors/5', headers=self.h_casting_director)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'bad request!')

    def test_get_movies_by_actor(self):
        res = self.client().get('/actor/1/movies', headers=self.h_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['current_actor'])

    def test_404_fail_get_movies_by_actor(self):
        res = self.client().get('/actor/2000/movies', headers=self.h_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found!')

    def test_get_actors_by_movie(self):
        res = self.client().get('/movie/1/actors', headers=self.h_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['current_movie'])

    def test_404_fail_get_actors_by_movie(self):
        res = self.client().get('/movie/2000/actors', headers=self.h_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found!')

    def test_add_association(self):
        res = self.client().post('/association', headers=self.h_executive_producer, json={
            "actor_id": 4,
            "movie_id": 4
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
