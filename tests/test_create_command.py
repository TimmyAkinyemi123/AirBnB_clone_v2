import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models import storage


class TestCreateCommand(unittest.TestCase):
    """Test cases for the create command."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_state_present(self, mock_stdout):
        """Test create State name="California" is present."""
        HBNBCommand().onecmd('create State name="California"')
        state_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(state_id) == 36)
        self.assertIsInstance(storage.all()['State.' + state_id], State)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_city_and_state_present(self, mock_stdout):
        """Test create State name="California" + create City state_id="<new state ID>" name="Fremont" is present."""
        HBNBCommand().onecmd('create State name="California"')
        state_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(state_id) == 36)
        self.assertIsInstance(storage.all()['State.' + state_id], State)

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        HBNBCommand().onecmd(f'create City state_id="{state_id}" name="Fremont"')
        city_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(city_id) == 36)
        self.assertIsInstance(storage.all()['City.' + city_id], City)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_city_with_space_in_name(self, mock_stdout):
        """Test create City state_id="<new state ID>" name="San_Francisco" is present (space translated to _)."""
        HBNBCommand().onecmd('create State name="California"')
        state_id = mock_stdout.getvalue().strip()

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        HBNBCommand().onecmd(f'create City state_id="{state_id}" name="San_Francisco"')
        city_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(city_id) == 36)
        self.assertIsInstance(storage.all()['City.' + city_id], City)
        self.assertEqual(storage.all()['City.' + city_id].name, 'San Francisco')


if __name__ == '__main__':
    unittest.main()
