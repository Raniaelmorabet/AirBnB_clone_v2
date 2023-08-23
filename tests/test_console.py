#!/usr/bin/python3
"""
Contains the class TestConsoleFunctionality
"""

import console
import pep8
import unittest
from unittest.mock import patch
import io

HBNBCommand = console.HBNBCommand

class TestConsoleFunctionality(unittest.TestCase):
    """Class for testing functionality of the console"""
    
    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_state(self, mock_stdout):
        # Test create State command with parameters
        self.console.onecmd('create State name="California"')
        created_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(created_id) > 0)

        obj = storage.get("State", created_id)
        self.assertEqual(obj.name, "California")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_place(self, mock_stdout):
        # Test create Place command with parameters
        self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        created_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(created_id) > 0)

        obj = storage.get("Place", created_id)
        self.assertEqual(obj.name, "My_little_house")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_state(self, mock_stdout):
        # Test show State command
        self.console.onecmd('show State')
        self.assertTrue("missing class name" in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all_state(self, mock_stdout):
        # Test all State command
        self.console.onecmd('all State')
        self.assertTrue("[]" in mock_stdout.getvalue())

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

if __name__ == '__main__':
    unittest.main()
