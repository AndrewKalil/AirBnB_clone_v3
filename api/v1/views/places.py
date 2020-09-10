
#!/usr/bin/python3
""" comment """
from api.v1.views import app_views
from flask import jsonify, make_response, abort, request
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
classes = {Amenity: "amenities", City: "cities", Place: "places",
    Review: "reviews", State: "state", User: "users"}
res = {"amenities": 0, "cities": 0, "places": 0,
    "reviews": 0, "states": 0, "users": 0}


@app_views.route('/cities', strict_slashes=False, methods=["GET"], defaults={"city_id": None})
@app_views.route('/cities/<city_id>/places', strict_slashes=False, methods=["GET"])
def ret_number_obj_get_pl(city_id):
	"""x function"""
	states_av = storage.all(City)
	for k, v in storage.all(City).items():
		if v.id == city_id:
			return jsonify([v.to_dict() for k, v in v.places])
	return make_response(jsonify({"error": "Not found"}), 404)


@app_views.route('/place/<place_id>', strict_slashes=False, methods=["GET"], defaults={"place_id": None}))
def ret_number_obj_get_pl(place_id):
	"""x function"""
	states_av=storage.all(Place)
	for k, v in storage.all(Place).items():
		if v.id == place_id:
			return make_response(jsonify(v.to_dict()))
	return make_response(jsonify({"error": "Not found"}), 404)


@app_views.route('/cities/<city_id>/places', strict_slashes = False, methods = ["POST"])
def ret_number_obj_post_Am():
	"""x function"""
	# validate if json is valid
	json_body=request.get_json(force = True, silent = True)
	if not json_body:
		abort(400, 'Not a Json')

	# if name is not in json_bodu
	if "user_id" not in json_body.keys():
		abort(400, 'Missing user_id')
	if "name" not in json_body.keys():
		abort(400, 'Missing name')

	# create object
	creat_ob=Place(**json_body)
	creat_ob.save()

	# Check if cit_id is FOUND
	states_av=storage.all(City)
	for k, v in storage.all(City).items():
		if v.id == city_id:
			v.places.append(creat_ob)
			return make_response(jsonify(creat_ob.to_dict()), 201)
	return make_response(jsonify({"error": "Not found"}), 404)


@app_views.route('/places/<place_id>', strict_slashes = False, methods = ["DELETE"])
def ret_number_obj_delete_pl(place_id):
	"""x function"""
	# validate if json is valid

	# if id is not present
	obj_=storage.get(Place, place_id)
	if obj_:
		storage.delete(obj_)
		storage.save()
		return make_response(jsonify({}), 200)

	else:
		return make_response(jsonify({"error": "Not found"}), 404)


@app_views.route('/places/<place_id>', strict_slashes = False, methods = ["PUT"])
def ret_number_obj_put_pl(place_id):
	"""x function"""
	# validate if json is valid
	json_body=request.get_json(force = True, silent = True)
	if not json_body:
		abort(400, 'Not a Json')

	obj_=storage.get(Place, place_id)
	if obj_:
		for k, v in json_body.items():
			if hasattr(obj_, k):
				setattr(obj_, k,  v)
		obj_.save()
		return make_response(jsonify(obj_.to_dict()), 200)
	else:
		return make_response(jsonify({"error": "Not found"}), 404)
