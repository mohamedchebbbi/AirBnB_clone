#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)

    def test_str(self):
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, old_updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        obj_dict = my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['name'], 'My_First_Model')
        self.assertEqual(obj_dict['my_number'], 89)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

        created_at_str = obj_dict['created_at']
        created_at_dt = datetime.strptime(created_at_str, '%Y-%m-%dT%H:%M:%S.%f')
        self.assertIsInstance(created_at_dt, datetime)
        self.assertEqual(created_at_dt, my_model.created_at)

    def test_from_dict(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertIsInstance(my_new_model.created_at, datetime)

if __name__ == '__main__':
    unittest.main()
