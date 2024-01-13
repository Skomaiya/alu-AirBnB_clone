#!/usr/bin/python3
"""
Created the Module: BaseModel
"""
import models
from uuid import uuid4
from datetime import datetime
 

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            Note: *args is not used for this project.
            **kwargs: Arbitrary keyword arguments.

        Note:
            If kwargs is not empty, it loads attributes from a dictionary.
            Otherwise, it generates a new id and timestamps.

        Attributes:
            id (str): A unique identifier generated using uuid4().
            created_at (datetime): The creation timestamp.
            updated_at (datetime): The last update timestamp.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' attribute to the current timestamp and saves to storage.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Converts the object's attributes to a dictionary.

        Returns:
            dict: A dictionary representation of the object.
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string containing the class name, id, and attribute dictionary.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
