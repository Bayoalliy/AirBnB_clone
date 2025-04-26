#!/usr/bin/python3
"""
Write a class City that inherits from BaseModel:

models/city.py
Public class attributes:
name: string - empty string
state_id: string - empty string: it will be the State.id
Update FileStorage to manage correctly serialization and
deserialization of City.

Update your command interpreter (console.py) to allow show,
create, destroy, update and all used with City.
"""
from models.base_model import BaseModel
from models import storage


class City(BaseModel):
    """inherits from BaseModel and defines the city object"""
    name = ""
    state_id = ""
