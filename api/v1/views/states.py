#!/usr/bin/python3
""" handles all default RestFul Api for States"""
from api.v1.views import app_views
from api.v1.views import *
from flask import jsonify, make_response, abort, request
from models import storage
from models.state import State

from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {Amenity: "amenities", City: "cities",Place: "places", Review: "reviews", State: "state", User: "users"}
res = {"amenities": 0, "cities": 0,"places": 0, "reviews": 0, "states": 0, "users": 0}


@app_views.route('/states', strict_slashes=False, methods = ["GET"], defaults = {"state_id":None})
@app_views.route('/states/<state_id>', strict_slashes=False, methods = ["GET"])
def ret_number_obj_get(state_id):
	"""x function"""
	if state_id is None:
		return jsonify([ obj_.to_dict() for k, obj_ in storage.all(State).items()])
	states_av = storage.all(State)
	for k, v in storage.all(State).items():
		if v.id == state_id:
			return jsonify(v.to_dict())
	return make_response(jsonify({"error": 404}), 404)



@app_views.route('/states', strict_slashes=False, methods = ["POST"])
def ret_number_obj_post():
	"""x function"""
	#validate if json is valid
	json_body = request.get_json(force = True, silent=True)
	if not json_body:
		abort(400, 'Not a Json')

	#if name is not in json_bodu
	if "name" not in json_body.keys():
		abort(400, 'Missing name')

	#create object
	creat_ob = State(**json_body)
	creat_ob.save()
	return make_response(jsonify(creat_ob.to_dict()), 201)

@app_views.route('/states/<state_id>', strict_slashes=False, methods = ["DELETE"])
def ret_number_obj_delete(state_id):
	"""x function"""
	#validate if json is valid

	#if id is not present
	obj_ = storage.get(State, state_id)
	if obj_:
		storage.delete(obj_)
		storage.save()
		return make_response(jsonify({}), 200)

	else:
		return make_response(jsonify({"error": "Not found"}), 404)



@app_views.route('/states/<state_id>', strict_slashes=False, methods = ["PUT"])
def ret_number_obj_put(state_id):
	"""x function"""
	#validate if json is valid
	json_body = request.get_json(force = True, silent=True)
	if not json_body:
		abort(400, 'Not a Json')

	#if name is not in json_bodu
	if "name" not in json_body.keys():
		abort(400, 'Missing name')
	obj_ = storage.get(State, state_id)
	if obj_:
		for k,v in json_body.items():
			if hasattr(obj_, k):
				setattr(obj_, k,  v)
		obj_.save()
		return make_response(jsonify(obj_.to_dict()), 200)
	else:
		return make_response(jsonify({"error": "Not found"}), 404)

