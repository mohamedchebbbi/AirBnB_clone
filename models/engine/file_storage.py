#!/usr/bin/python3

import json

class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionnary __objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file exists)."""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                loaded_objs = json.load(f)
                for key, value in loaded_objs.items():
                    cls_name, obj_id = key.split(".")
                    cls = eval(cls_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
