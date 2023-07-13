#!/usr/bin/python3
""" ___init magic method for models directori. """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
