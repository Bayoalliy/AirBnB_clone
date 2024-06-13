#!/usr/bin/python3
"""
This module defines the user class,
a subclass of BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ definition of User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
