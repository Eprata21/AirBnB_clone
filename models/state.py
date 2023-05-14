#!/usr/bin/python3
"""class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """rep of state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """init state"""
        super().__init__(*args, **kwargs)
