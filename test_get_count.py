#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from models.amenity import Amenity
#print("All objects: {}".format(storage.count()))
#print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
#print(first_state_id)
#print ( [ obj_.to_dict() for k, obj_ in storage.all(State).items()] )
print ( [ obj_.to_dict() for k, obj_ in storage.all(Amenity).items()] )

#print("First state: {}".format(storage.get(State, first_state_id)))
#print("First state: {}".format(storage.get(None, first_state_id)))
