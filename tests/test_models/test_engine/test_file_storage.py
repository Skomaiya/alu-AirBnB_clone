#!/usr/bin/python3
"""
Created the TestFileStorage
"""

import json
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorageInstatiation(unittest.TestCase):
    """
    Test cases for FileStorage instantiation.
    """
    def test_FileStorage_instantiation_no_args(self):
        """
        Test FileStorage instantiation with no arguments.
        """
        self.assertEqual(type(FileStorage()), FileStorage)
        
    def test_FileStorage_instantiation_with_args(self):
        """
        Test FileStorage instantiation with arguments.
        """
        with self.assertRaises(TypeError):
            FileStorage(None)
            
    def test_FileStorage_initializes(self):
        """
        Test that models.storage initializes as FileStorage.
        """
        self.assertEqual(type(models.storage), FileStorage)
        
class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage methods.
    """
    
    def setUp(self):
        self.test_file = "test_file.json"
        
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        
    def test_all_storage_returns_dictionary(self):
        """
        Test that models.storage.all() returns a dictionary.
        """
        self.assertEqual(dict, type(models.storage.all()))
        
    def test_new(self):
        """
        Test models.storage.new() method.
        """
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())
        
    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)    
    
    def test_new_with_args(self):
        """
        Test models.storage.new() method with arguments.
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)
            
    def test_new_with_None(self):
        """
        Test models.storage.new() method with None.
        """
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        models.storage.new(obj_1)
        models.storage.new(obj_2)
        models.storage.save()
        
        new_storage = FileStorage()
        new_storage.reload()
        
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj_1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj_2.id)) is not None)
        
    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)
        
    def test_save_to_file(self):
        """
        Test models.storage.save() method and file creation.
        """
        new_obj_1 = BaseModel()
        models.storage.new(new_obj_1)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))
        
    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)
        
    def test_reload_empty_file(self):
        """
        Test models.storage.reload() method with an empty file.
        """
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()
            
    def test_reload_no_file(self):
        print("Current working directory:", os.getcwd())
        print("Contents of the directory:", os.listdir())
        with self.assertRaises(FileNotFoundError):
            models.storage.reload()

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == '__main__':
    unittest.main()

