#!/usr/bin/python3
"""
Created the TestFileStorage
"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

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
        new_obj = BaseModel()
        models.storage.new(new_obj)
        self.assertIn("BaseModel.{}".format(new_obj.id), models.storage.all())
        
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
        
    def test_save_to_file(self):
        """
        Test models.storage.save() method and file creation.
        """
        new_obj_1 = BaseModel()
        models.storage.new(new_obj_1)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))
        
    def test_reload_empty_file(self):
        """
        Test models.storage.reload() method with an empty file.
        """
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()

if __name__ == '__main__':
    unittest.main()

