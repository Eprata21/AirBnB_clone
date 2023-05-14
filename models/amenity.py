#!/usr/bin/python3
"""class amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """rep of amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """init amenity"""
        super().__init__(*args, **kwargs)
