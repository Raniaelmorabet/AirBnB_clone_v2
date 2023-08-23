import unittest
from unittest.mock import patch
from console import HBNBCommand
import io

class TestConsoleCreateParams(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_with_string_value(self, mock_stdout):
        self.console.onecmd('create State name="California"')
        created_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(created_id) > 0)

        obj = storage.get("State", created_id)
        self.assertEqual(obj.name, "California")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_with_float_value(self, mock_stdout):
        self.console.onecmd('create Place price_by_night=120.50')
        created_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(created_id) > 0)

        obj = storage.get("Place", created_id)
        self.assertEqual(obj.price_by_night, 120.50)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_with_integer_value(self, mock_stdout):
        self.console.onecmd('create Place number_rooms=3')
        created_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(created_id) > 0)

        obj = storage.get("Place", created_id)
        self.assertEqual(obj.number_rooms, 3)

if __name__ == '__main__':
    unittest.main()
