from django.test import TestCase
from app.calc import add

class CalcTests(TestCase):

    def test_add(self):
        """Checking if I know how to write a add method"""
        self.assertEquals(add(1,1), 2)
