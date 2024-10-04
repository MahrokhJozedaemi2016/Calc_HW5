import unittest
from app.commands.subtract_command import SubtractCommand

class TestSubtractCommand(unittest.TestCase):
    def test_subtract(self):
        subtract_command = SubtractCommand()
        self.assertEqual(subtract_command.execute(10, 2), 8)
        self.assertEqual(subtract_command.execute(5, 5), 0)
        self.assertEqual(subtract_command.execute(-5, -5), 0)
        self.assertEqual(subtract_command.execute(0, 10), -10)

if __name__ == '__main__':
    unittest.main()

