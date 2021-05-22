import unittest
from unittest.mock import patch
import advanced


# Create some test cases for the methods that you want to test
# For that create a test class which inherits unittest.TestCase
# to get different capabilities of testing

class TestAdvanced(unittest.TestCase):

    # define a test method whose must start with 'test_' so that
    # compiler know which are the test methods.
    def test_add(self):
        # There are different assert methods that can be used for testing
        self.assertEqual(advanced.add(20, 19), 39)
        self.assertEqual(advanced.add(-2, -1), -3)
        self.assertEqual(advanced.add(-1, 0), -1)

    def test_sub(self):
        # There are different assert methods that can be used for testing
        self.assertEqual(advanced.sub(20, 19), 1)
        self.assertEqual(advanced.sub(-2, -1), -1)
        self.assertEqual(advanced.sub(-1, 0), -1)

    def test_multiply(self):
        # There are different assert methods that can be used for testing
        self.assertEqual(advanced.multiply(20, 10), 200)
        self.assertEqual(advanced.multiply(-20, -10), 200)
        self.assertEqual(advanced.multiply(-20, 10), -200)

    def test_divide(self):
        # There are different assert methods that can be used for testing
        self.assertEqual(advanced.divide(20, 10), 2)
        self.assertEqual(advanced.divide(-2, -0.5), 4)
        self.assertEqual(advanced.divide(-1, 1), -1)

        # To test the raised error in the code is expected error
        # METHOD - 1:
        # ____________
        self.assertRaises(ZeroDivisionError, advanced.divide, 20, 0)

        # METHOD - 2:
        # ____________
        with self.assertRaises(ZeroDivisionError):
            advanced.divide(20, 0)


class TestEmployee(unittest.TestCase):

    # It run at the very beginning of every tests
    @classmethod
    def setUpClass(cls):
        print('setUpClass', end='\n\n')

    # It run at the very ending of every tests
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # It will run before every single test
    def setUp(self):
        print('setUp')
        self.emp1 = advanced.Employee('Subhash', 'Swansi', 60000)
        self.emp2 = advanced.Employee('Samar', 'Verma', 50000)

    # It wi ll run after each single test
    def tearDown(self):
        print('tearDown', end='\n\n')

    def test_email(self):
        self.assertEqual(self.emp1.email, 'Subhash.Swansi@gmail.com')
        self.assertEqual(self.emp2.email, 'Samar.Verma@gmail.com')

        self.emp1.first_name = 'kalki'
        self.emp2.first_name = 'Aman'

        self.assertEqual(self.emp1.email, 'kalki.Swansi@gmail.com')
        self.assertEqual(self.emp2.email, 'Aman.Verma@gmail.com')

    def test_username(self):
        self.assertEqual(self.emp1.username, 'Subhash Swansi')
        self.assertEqual(self.emp2.username, 'Samar Verma')

        self.emp1.first_name = 'kalki'
        self.emp2.first_name = 'Aman'

        self.assertEqual(self.emp1.username, 'kalki Swansi')
        self.assertEqual(self.emp2.username, 'Aman Verma')

    def test_apply_raise(self):
        self.emp1.apply_raise()
        self.emp2.apply_raise()
        self.assertEqual(self.emp1.pay, 63000)
        self.assertEqual(self.emp2.pay, 52500)

    def test_monthly_schedule(self):
        # using patch as a context manager
        # we are mocking requests.get of advanced module as mocked_get
        with patch('advanced.requests.get') as mocked_get:
            # Instead of going to the website we can test for successful
            # call using :-
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp1.monthly_schedule('May')
            # mocked_get.assert_callled_with('http://company.com/Swansi/May')
            self.assertEqual(schedule, 'Success')

            # To test a failed response :
            # text will be 'Bad Response'
            mocked_get.return_value.ok = False

            schedule = self.emp1.monthly_schedule('August')
            # mocked_get.assert_callled_with('http://company.com/Swansi/May')
            self.assertEqual(schedule, 'Bad Response!')


# To test we can use command : python -m unittest test_advanced.py
# OR we can print the  test result in console using following codes :
if __name__ == '__main__':
    unittest.main()
