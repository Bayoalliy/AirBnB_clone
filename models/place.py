#!/usr/bin/python3
"""
Write a class Review that inherits from BaseModel:

models/review.py
Public class attributes:
place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string

Update FileStorage to manage correctly serialization and
deserialization of Review.

Update your command interpreter (console.py) to allow show,
create, destroy, update and all used with Review.
"""
from models.base_model import BaseModel
from models import storage


class Review(BaseModel):
    """inherits from BaseModel and defines the review object"""
    place_id = ""
    user_id = ""
    text = ""
