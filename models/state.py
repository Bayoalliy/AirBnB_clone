#!/usr/bin/python3
"""
Write a class State that inherits from BaseModel:

models/state.py
Public class attributes:
name: string - empty string

Update FileStorage to manage correctly serialization and
deserialization of State.

Update your command interpreter (console.py) to allow show,
create, destroy, update and all used with State.
"""
from models.base_model import BaseModel
from models import storage


class State(BaseModel):
    """inherits from BaseModel and defines the state object"""
    name = ""
