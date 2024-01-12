#!/usr/bin/python3
"""
Created the Module: file_storage
"""
import json
import os
from models.base_model import BaseModel
import models

class FileStorage:
    """
    Handles the serialization and deserialization of instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store serialized instances.
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj (BaseModel): The object to be added.
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns the dictionary of serialized objects.

        Returns:
            dict: A dictionary containing serialized objects.
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes objects and saves them to a JSON file.
        """
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj_key, obj_instance in all_objs.items():
            obj_dict[obj_key] = obj_instance.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """
        Deserializes objects from the JSON file and loads them into the storage.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as json_file:
                try:
                    obj_dict = json.load(json_file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)
                        FileStorage.__objects[key] = instance

                except Exception:
                    pass
