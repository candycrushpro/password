import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    test class for behaviors

    Args:
        unittest.TestCase : Test case that helps in creating test cases

    '''

    def setUp(self):
        '''
        method run before each test case
        '''

        self.new_user = User("Bradley","password")

    
      