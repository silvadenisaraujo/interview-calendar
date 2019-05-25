# application/__init__.py
from flask import request, jsonify
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from application.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/interviewer/', methods=['POST', 'GET'])
    def interviewer():
        from application import services
        if request.method == 'POST':
            result = services.create_interviewer(request.data)
            response = jsonify(result)
            return response
        elif request.method == 'GET':
            result = services.list_interviewers()
            response = jsonify(result)
            return response

    @app.route('/interviewee/', methods=['POST', 'GET'])
    def interviewee():
        from application import services
        if request.method == 'POST':
            result = services.create_interviewee(request.data)
            response = jsonify(result)
            if result:
                response.status_code = 200
                return response
            else:
                response.status_code = 400
            return response
        elif request.method == 'GET':
            result = services.list_interviewees()
            response = jsonify(result)
            response.status_code = 200
            return response

    @app.route('/interview/', methods=['POST', 'GET'])
    def interview():
        from application import services
        if request.method == 'POST':
            result = services.create_interview(request.data)
            response = jsonify(result)
            if result:
                response.status_code = 201
                return response
            else:
                response.status_code = 400
            return response
        elif request.method == 'GET':
            result = services.list_interviews()
            response = jsonify(result)
            response.status_code = 200
            return response

    return app

