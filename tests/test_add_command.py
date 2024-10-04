import unittest
from calculator.commands.add_command import AddCommand

class TestAddCommand(unittest.TestCase):
    def test_add(self):
        add_command = AddCommand()
        self.assertEqual(add_command.execute(2, 3), 5)
        self.assertEqual(add_command.execute(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
