#!/usr/bin/python3
"""__init__ magic method for models directory"""
from model.engine.filestorage import file_storage

storage = file_storage()

storage.reload()
