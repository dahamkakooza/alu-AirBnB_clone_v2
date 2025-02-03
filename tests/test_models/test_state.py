#!/usr/bin/python3
"""State class test module"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State

class test_state(test_basemodel):
   """Test State class"""
   
   def __init__(self, *args, **kwargs):
       """Initialize test class"""
       super().__init__(*args, **kwargs)
       self.name = "State" 
       self.value = State
       
   def test_name3(self):
       """Test name attribute type"""
       new = self.value()
       new.name = "Test State"  # Initialize name
       self.assertEqual(type(new.name), str)