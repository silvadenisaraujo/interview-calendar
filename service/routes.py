from service import app
from flask import request


@app.route('/interviewer', methods=['POST'])
def slots():
    data = request.get_json()
    print(data)
    return ""


@app.route('/')
def index():
    return ""
