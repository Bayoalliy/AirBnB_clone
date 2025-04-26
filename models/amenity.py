#!/usr/bin/python3
"""
Write a class Amenity that inherits from BaseModel:

models/amenity.py
Public class attributes:
name: string - empty string
Update FileStorage to manage correctly serialization and
deserialization of Amenity.

Update your command interpreter (console.py) to allow show,
create, destroy, update and all used with Amenity.
"""
from models.base_model import BaseModel
from models import storage


class Amenity(BaseModel):
    """inherits from BaseModel and defines the Amenity object"""
    name = ""
