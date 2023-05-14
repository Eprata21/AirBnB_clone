#!/usr/bin/python3
"""Base Model"""

import models
import json
import uuid
from datetime import datetime

format = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
        """BaseModel for other classes"""

        def __init__(self, *args, **kwargs):
                """public instance attr"""
                if kwargs:
                    self.__dict__ = kwargs
                    if "created_at" in kwargs:
                        self.created_at = datetime.strptime(kwargs.get("created_at"), format)
                    if "updated_at" in kwargs:
                        self.updated_at = datetime.strptime(kwargs.get("updated_at"), format)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at =datetime.now()
                    models.storage.new(self)

        def __str__(self):
                """String rep of the BaseModel"""
                return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

        def save(self):
                """updates the attr updated_at"""
                self.updated_at = datetime.now()
                models.storage.save()

        def to_dict(self):
                """returns a dictionary with created_at and updated_at"""
                my_dict = self.__dict__.copy()
                my_dict['__class__'] = self.__class__.__name__
                my_dict['created_at'] = my_dict['created_at'].isoformat()
                my_dict['updated_at'] = my_dict['updated_at'].isoformat()
                return my_dict
