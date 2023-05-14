import uuid
from datetime import datetime

formatt = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
        """BaseModel for other classes"""

        def __init__(self, *args, **kwargs):
                """public instance attr"""
                if kwargs:
                        for key, value in kwargs.items():
                               if key == "created_at" or key == "updated_at":
                                      value = datetime.strptime(value, formatt)
                               if key != "__class__":
                                      setattr(self, key, value)
                                               
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at =datetime.now()
                    models.storage.new(self)

        def __str__(self):
                """String rep of the BaseModel"""
                return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

        def save(self):
                """updates the attr updated_at"""
                self.updated_at = datetime.now()
                models.storage.save()

        def to_dict(self):
                """returns a dictionary with created_at and updated_at"""
                ob_dict = self.__dict__.copy()
                ob_dict['__class__'] = self.__class__.__name__
                ob_dict['created_at'] = self.created_at.isoformat()
                ob_dict['updated_at'] = self.updated_at.isoformat()
                return ob_dict
