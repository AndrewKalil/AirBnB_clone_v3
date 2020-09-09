from api.v1.views import app_views
from models import storage

from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
classes = {Amenity: "amenities", City: "cities",Place: "places", Review: "reviews", State: "state", User: "users"}
@app_views.route('/status', strict_slashes=False)
def ret_json():
	"""x function"""
	return {"status": "OK"}

@app_views.route('/stats', strict_slashes=False)
def ret_number_objects():
	"""x function"""
	objs = storage.count()
	res = {"amenities": 0, "cities": 0,"places": 0, "reviews": 0, "states": 0, "users": 0}

	for cls_obj, cls_str_res in classes.items():
		res[cls_str_res] = storage.count(cls_obj)
	return res
		
