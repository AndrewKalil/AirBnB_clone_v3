from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def ret_json():
	"""x function"""
	return {"status": "OK"}
