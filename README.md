# Full Stack Casting Agency API Backend
This is a backend-api for Casting Agency as my capstone graduation project in Udacity-FSND. The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. 

## Getting Started
- Live version: [Casting Agency](https://casting-agency-hos-fsnd.herokuapp.com/)
- Register & login: [Auth0](https://hos-casting-agency.us.auth0.com/authorize?audience=Agency&response_type=token&client_id=S4I2zzlySvWwpopBB16inKCEap2wPR5J&redirect_uri=https://casting-agency-hos-fsnd.herokuapp.com/login-results)

### Installing Dependencies

#### Python 3.8

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
## Unit Testing

To run the tests open your terminal and run:

```bash
dropdb Agency
createdb Agency
```
then insert some fake data before test you can generate some from [Mockaroo](https://www.mockaroo.com/)
as there are three tables:
- actors contains two main columns: name and age. 
- movies contains two cloumns: title and release_date. 
- association contains two cloumns: actor_id and movie_id.


then run 
```bash
python test_app.py
```
## Testing End Points

Export these variables in your terminal before testing end points.

These variables refere to three roles for this api:
- Assistant: Castint Asistant.
- Director: Casting Director.
- Producer: Executive Producer.

```bash
export Assistant='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk1UktCWlhaRnpranphaElrLWlnZCJ9.eyJpc3MiOiJodHRwczovL2hvcy1jYXN0aW5nLWFnZW5jeS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxNzRjYzhkYmY2ZmYwMDEzNWNhMTFiIiwiYXVkIjoiQWdlbmN5IiwiaWF0IjoxNTk1MzcxMDAwLCJleHAiOjE1OTU0NTc0MDAsImF6cCI6IlM0STJ6emx5U3ZXd3BvcEJCMTZpbktDRWFwMndQUjVKIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.CTt3bzlrohc1FNN4uj1MPZnFqdfPLuekxFTgg3LtL1n5mGPSZ2OhIxEU-hdL4pHOsaRyW6nqnSNKAL9GkSdlj2hNlZFg1F8rJaALuoUbXDe71r-wUV1-0ZsCC2quVHwwdgd0taUYPiOVAKobipflotsJ3yKhV7gsOIhvWHTCbTFdMm2FtojlF4W2U1LoczV0GvWQZS_ikHw_QQqwzDW6c1V_6ryi4wYD9Z96qLgbBlOFZECLQFn5fBie4qNXArGMFbVcSuzZ7Fn3xMi7V9xlPrez5GNwzCMCp_wQgmrQ_f_UTrCxfjpmhgJbGHRmeDL4vpjFrcxMz92ldsfglBYBwg'

export Director='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk1UktCWlhaRnpranphaElrLWlnZCJ9.eyJpc3MiOiJodHRwczovL2hvcy1jYXN0aW5nLWFnZW5jeS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxNzRjYTYyYWQzMmMwMDEzNTAxNTA4IiwiYXVkIjoiQWdlbmN5IiwiaWF0IjoxNTk1MzcwNjU1LCJleHAiOjE1OTU0NTcwNTUsImF6cCI6IlM0STJ6emx5U3ZXd3BvcEJCMTZpbktDRWFwMndQUjVKIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.YEb578kyZrctRbujATv57izuiIyTN1DXZN8bJL05YhjDx5uEV7X4f3CpBSTAvvs7CwwWD58_5bogWh6P3Die_z7pGUkWnIxzWsYTHeLLD0WNU5AoczgRg93OgPzuidaoFYoUmkeJ66u8-f_o-hNe1HAHI9zHB3ao7yPKzibkYdGC3Jfwv7QYH7mZpMFQaIa88SBJVLmNWh5ujiSWRXKWJmeb8ynIjsBE4N8oo5niX6OkkqIaolj1qtbyFGKvgbJ3n3yPnQ7QN2vT7_EieLAWkYYMrme7PTbWAtN1_06F0g6QzcjxL5nRB3gC-vaFX6omZxztkM9NzmtBhkT6tn4sqg'

export Producer='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk1UktCWlhaRnpranphaElrLWlnZCJ9.eyJpc3MiOiJodHRwczovL2hvcy1jYXN0aW5nLWFnZW5jeS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ4Nzg3MzgwODkwODk1ODA0NTIiLCJhdWQiOlsiQWdlbmN5IiwiaHR0cHM6Ly9ob3MtY2FzdGluZy1hZ2VuY3kudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5NTM3MTEzMCwiZXhwIjoxNTk1NDU3NTMwLCJhenAiOiJTNEkyenpseVN2V3dwb3BCQjE2aW5LQ0VhcDJ3UFI1SiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0OmFzc29jaWF0aW9ucyIsInBvc3Q6bW92aWVzIl19.XETQyRM1ZzjIEnFqo4bswXv2mOJpXUUgWLQkJncR8kEVnOWOENTjl6_-WIWBl8y7d3GcjOQVgyUd-xD20rOOyhqe6YPLxvZeBW-PxU25rCwPQ4t5IBExz4Ggn0DQF9w3r0YJ-Cqm0-rqVIz5fTP-IvBWdiKMwpOZyMrCKRc0WxzvlHk6nAK6SGLUIO9M9P0fhZQGDM6AzpSOPUfiqRjlu6TR5kXXQ0DhpXhMx5ur_tJddpVjaLzmabs8JBdtSKGnVklguurq9K8b5YuzWJDgD9h7ot3pLdD6sC-Nw9_ezyI3bMAHEmvtYf4Mgz4J-_Rdl6Lap7I2oOMaBSlp27a-1w'
```



## Error Handling
Errors are returned in the following format as a JSON objects:
```
{
  "success": False,
  "error": 404,
  "message": "Not Found!"
}
```

The API will return four error types when requests fail:
- 404: Not found.
- 400: Bad request.
- 405: Not allowed.
- 422: Unprocessable.

## End points 

### GET '/categories'
- Request Arguments: None
- Returns a list of movies objects, success value and total movies.
- Authorization: <strong>Casting Assistant, Casting Director and Executive Prodeucer</strong>

#### sample
`curl -H "Authorization: Bearer ${Assistant}" https://casting-agency-hos-fsnd.herokuapp.com/movies`
```
{
{
  "movies": [
    {
      "id": 1, 
      "release_date": "Wed, 13 Nov 2019 22:48:05 GMT", 
      "title": "Liliom"
    }, 
    {
      "id": 2, 
      "release_date": "Thu, 05 Dec 2019 12:19:58 GMT", 
      "title": "test"
    }, 
    .........
  ], 
  "success": true, 
  "total_movies": 20
}

}
```

### GET '/actors'
- Request Arguments: None
- Returns a list of actors objects, success value and total actors.
- Authorization: <strong>Casting Assistant, Casting Director and Executive Prodeucer</strong>

#### sample
`curl -H "Authorization: Bearer ${Assistant}" https://casting-agency-hos-fsnd.herokuapp.com/actors`

```
{
  "actors": [
    {
      "age": 25, 
      "id": 1, 
      "name": "Salli"
    }, 
    {
      "age": 30, 
      "id": 2, 
      "name": "Elissa"
    }, 
    {
      "age": 40, 
      "id": 3, 
      "name": "Franni"
    }, 
    ..............
  ], 
  "success": true, 
  "total_actors": 20
}
```

### GET '/actor/<actor_id>/movies'
- Request Arguments: actor_id
- Returns a list of movies associated with this actor.
- Authorization: <strong>Casting Assistant, Casting Director and Executive Prodeucer</strong>.

#### sample
`curl -H "Authorization: Bearer ${Assistant}" https://casting-agency-hos-fsnd.herokuapp.com/actor/1/movies`

```
{
  "current_actor": "Salli", 
  "movies": [
    {
      "id": 20, 
      "release_date": "Fri, 06 Sep 2019 09:26:03 GMT", 
      "title": "American Idiots"
    }
  ], 
  "success": true
}
```
### GET '/movie/<movie_id>/actorss'
- Request Arguments: movie_id
- Returns a list of actors associated with this movie.
- Authorization: <strong>Casting Assistant, Casting Director and Executive Prodeucer</strong>.

#### sample
`curl -H "Authorization: Bearer ${Assistant}" https://casting-agency-hos-fsnd.herokuapp.com/movie/1/actors`

```
{
  "actors": [
    {
      "age": 33, 
      "id": 14, 
      "name": "Jose"
    }
  ], 
  "current_movie": "Liliom", 
  "success": true
}
```

### POST'/movies'
- Creates a new movie using the submitted title and realease_date. 
- Request Arguments: None
- Returns an object of three keys:
    * posted value: the id of the new movie.
    * success value.
    * no of total movies(after creation).
- Authorization: Only <strong>Executive Prodeucer</strong>.


#### sample 
`curl -H "Authorization: Bearer ${Producer}" https://casting-agency-hos-fsnd.herokuapp.com/movies -X POST -H "Content-Type: application/json" -d '{"title":"new movie", "release_date": "2020-07-22 04:26:08"}'`
```
{
  "posted": 21, 
  "success": true, 
  "total_movies": 21
}
```

### POST'/actors'
- Creates a new actor using the submitted name and age. 
- Request Arguments: None
- Returns an object of three keys:
    * posted value: the id of the new actor.
    * success value.
    * no of total actors(after creation).
- Authorization: <strong>Casting Director and Executive Prodeucer</strong>.


#### sample 
`curl -H "Authorization: Bearer ${Director}" https://casting-agency-hos-fsnd.herokuapp.com/actors -X POST -H "Content-Type: application/json" -d '{"name":"new actor", "age": "35"}'`
```
{
  "posted": 21, 
  "success": true, 
  "total_actors": 21
}
```

### DELETE'/movies/<movie_id>'
- Request Arguments: movie_id.
- Returns an object of three keys:
    * deleted value: the id of the deleted movie.
    * success value.
    * no of total movies (after deletion).
- Authorization: Only <strong>Executive Prodeucer</strong>.

#### sample
`curl -H "Authorization: Bearer ${Producer}" -X DELETE https://casting-agency-hos-fsnd.herokuapp.com/movies/6`
```
{
  "deleted": 6, 
  "success": true, 
  "total_movies": 20
}
```

### DELETE'/actors/<actor_id>'
- Request Arguments: actor_id.
- Returns an object of three keys:
    * deleted value: the id of the deleted actor.
    * success value.
    * no of total actors (after deletion).
- Authorization: <strong>Casting Director and Executive Prodeucer</strong>.

#### sample
`curl -H "Authorization: Bearer ${Director}" -X DELETE https://casting-agency-hos-fsnd.herokuapp.com/actors/6`
```
{
  "deleted": 6, 
  "success": true, 
  "total_actors": 20
}
```

### PATCH'/actors/<actor_id>'
- edit the actor name or age depends on the request body. 
- Request Arguments: actor id.
- Returns an object of three keys:
    * id value: the id of the actor.
    * success value.
- Authorization: <strong>Casting Director and Executive Prodeucer</strong>.

#### sample 
`curl -H "Authorization: Bearer ${Director}" https://casting-agency-hos-fsnd.herokuapp.com/actors/5 -X PATCH -H "Content-Type: application/json" -d '{"name":"changed name", "age": "39"}'`
```
{
  "id": "5", 
  "success": true
}
```

### PATCH'/movies/<movie_id>'
- edit the movie title or release_date depends on the request body. 
- Request Arguments: movie id.
- Returns an object of three keys:
    * id value: the id of the movie.
    * success value.
- Authorization: <strong>Casting Director and Executive Prodeucer</strong>.

#### sample 
`curl -H "Authorization: Bearer ${Director}" https://casting-agency-hos-fsnd.herokuapp.com/movies/5 -X PATCH -H "Content-Type: application/json" -d '{"title":"changed title"}'`
```
{
  "id": "5", 
  "success": true
}
```
