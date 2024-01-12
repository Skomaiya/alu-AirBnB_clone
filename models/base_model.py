#!/usr/bin/python3
"""
Created the Module: BaseModel
"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Attributes:
            id (str): A unique identifier generated using uuid4().
            created_at (datetime): The creation timestamp.
            updated_at (datetime): The last update timestamp.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the 'updated_at' attribute to the current timestamp.
        """
        self.updated_at = datetime.now()

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
