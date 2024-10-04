import unittest
from app.commands.divide_command import DivideCommand

class TestDivideCommand(unittest.TestCase):
    def test_divide(self):
        divide_command = DivideCommand()
        self.assertEqual(divide_command.execute(10, 2), 5)
        self.assertEqual(divide_command.execute(9, 3), 3)
        self.assertEqual(divide_command.execute(-9, 3), -3)
        self.assertAlmostEqual(divide_command.execute(7, 3), 7/3)  # Test non-integer division

    def test_divide_by_zero(self):
        divide_command = DivideCommand()
        with self.assertRaises(ValueError):
            divide_command.execute(10, 0)

if __name__ == '__main__':
    unittest.main()
