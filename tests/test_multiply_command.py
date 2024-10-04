import unittest
from calculator.commands.multiply_command import MultiplyCommand

class TestMultiplyCommand(unittest.TestCase):
    def test_multiply(self):
        multiply_command = MultiplyCommand()
        self.assertEqual(multiply_command.execute(3, 4), 12)
        self.assertEqual(multiply_command.execute(0, 10), 0)
        self.assertEqual(multiply_command.execute(-3, 3), -9)
        self.assertEqual(multiply_command.execute(-2, -2), 4)

if __name__ == '__main__':
    unittest.main()

