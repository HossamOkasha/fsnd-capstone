import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movie, Actor


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

    @app.route('/')
    def index():
        return 'developed by Hossam Okasha'
    return app