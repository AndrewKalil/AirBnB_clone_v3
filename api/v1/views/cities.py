#!/usr/bin/python3
""" handles all default RestFul API actions """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models import City

@app_views.route("/states/<uuid:state_id>/cities", methods=["GET"])
def get_all_cities_by_sate(state_id):
    """ Retrieves the list of all City objects of a State
    """
    if storage.get("State", state_id) is None:
        abort(404)
    city_list = []
    for key, value in storage.all("City").items():
        if value.state_id == str(state_id):
            city_list.append(value.to_dict())
    return jsonify(city_list)

@app_views.route("/cities/<uuid:city_id>", methods=["GET"])
def get_city_object(city_id):
    """ Retrieves a City object
    """
    try:
        return jsonify(storage.get("City", city_id).to_dict())
    except Exception:
        abort(404)

@app_views.route("/cities/<uuid:city_id>", methods=["DELETE"])
def delete_city_object(city_id):
    """ Deletes a City object
    """
    try:
        storage.delete(storage.get("City", city_id))
        storage.save()
        return jsonify({}), 200
    except Exception:
        abort(404)

@app_views.route("/states/<uuid:state_id>/cities", methods=["POST"])
def post_city(state_id):
    """ Creates a City Object
    """
    if storage.get("State", state_id) is None:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    city_dict = request.get_json()
    if "name" not in city_dict:
        return jsonify({"error": "Missing name"}), 400
    else:
        city_name = city_dict["name"]
        city = City(name=city_name, state_id=state_id)
        for key, value in city_dict.items():
            setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 201

@app_views.route("/cities/<uuid:city_id>", methods=["PUT"])
def put_city(city_id):
    """Updates a City object
    """
    ignore = ["id", "state_id", "created_at", "updated_at"]
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    json = request.get_json()
    for key, value in json.items():
        if key not in ignore:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict()), 200
