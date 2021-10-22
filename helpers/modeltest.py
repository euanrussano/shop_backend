import unittest
from django.test import TestCase

class APIModelTest:

    abstract = True

    @classmethod
    def setUpClass(cls):
        "Child classes must override this method and define cls.test_data, model"
        if cls.abstract:
            raise unittest.SkipTest("For some reason")
        super().setUpClass()
        
    def setUp(self):
        self.test_data.initializeData()

    def run_test_feature(self, id, feature_name, expected_value):
        test_id = id
        object = self.model.objects.get(id=test_id)
        initial_object_list = getattr(self.test_data, 'initial_' + self.model.__name__.lower())
        expected_value = str(initial_object_list[test_id-1][feature_name])
        current_value = str(object.price)
        self.assertEquals(expected_value, current_value)