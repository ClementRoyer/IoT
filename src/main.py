## init fingerprint

# from fingerprint import enroll_finger, get_fingerprint, delete
from fakeFingerPrint import enroll_finger, get_fingerprint, delete
from flask import Flask, request, make_response, jsonify
# from flask_restful import Resource, Api
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# api = Api(app)


fingers = []


class Finger:
    def __init__(self, id):
        self.id = id


class answer:
    def __init__(self, message, code):
        self.message = message
        self.code = code


def retFactory(msg, code):
    return jsonify(msg=msg, code = code), code


@app.route("/add", methods=['GET'])
def add():
    number = enroll_finger()
    print("n = ", number)
    if number in fingers:
        return jsonify(msg= 'Finger N°'+str(number)+' already added'), 409 ## Conflict
    fingers.append(number)
    return jsonify(msg= 'Finger N°'+str(number)+' added'), 200


@app.route('/exist', methods=['GET'])
def test():
    number = get_fingerprint()
    print("n = ", number)
    return retFactory('Finger N°'+str(number)+' OK', 200) if number in fingers else retFactory('Finger N°'+str(number)+' not found', 404)


@app.route('/delete', methods=['GET'])
def rm():
    number = get_fingerprint()
    print("n = ", number)
    if not number in fingers:
        return jsonify(msg='Finger N°'+str(number)+' not found'), 404 ## not found
    fingers.remove(number)
    return jsonify(msg='Finger N°'+str(number)+' deleted'), 200## success


@app.route('/list', methods=['GET'])
def list():
    _fingers = []
    for finger in fingers:
        _fingers.append(Finger(finger))
    other = json.dumps([ob.__dict__ for ob in _fingers])
    return make_response(other, 200)


app.run(host='0.0.0.0', port=8088)