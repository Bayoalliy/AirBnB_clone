#!/usr/bin/python3
"""
Write a class place that inherits from BaseModel:

models/place.py
Public class attributes:
city_id: string - empty string: it will be the City.id
user_id: string - empty string: it will be the User.id
name: string - empty string
description: string - empty string
number_rooms: integer - 0
number_bathrooms: integer - 0
max_guest: integer - 0
price_by_night: integer - 0
latitude: float - 0.0
longitude: float - 0.0
amenity_ids: list of string - empty list: it will be the list of Amenity.id later

Update FileStorage to manage correctly serialization and
deserialization of Place.

Update your command interpreter (console.py) to allow show,
create, destroy, update and all used with Place.
"""
from models.base_model import BaseModel
from models import storage


class Place(BaseModel):
    """inherits from BaseModel and defines the place object"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
