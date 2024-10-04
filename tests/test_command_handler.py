import unittest
from calculator.commands.command_handler import CommandHandler
from calculator.commands.add_command import AddCommand
from calculator.commands.subtract_command import SubtractCommand
from calculator.commands.multiply_command import MultiplyCommand
from calculator.commands.divide_command import DivideCommand

class TestCommandHandler(unittest.TestCase):
    def setUp(self):
        self.handler = CommandHandler()
        # Register some commands for testing
        self.handler.register_command('add', AddCommand())
        self.handler.register_command('subtract', SubtractCommand())
        self.handler.register_command('multiply', MultiplyCommand())
        self.handler.register_command('divide', DivideCommand())

    def test_register_and_execute_add(self):
        result = self.handler.execute_command('add', 2, 3)
        self.assertEqual(result, 5)

    def test_register_and_execute_subtract(self):
        result = self.handler.execute_command('subtract', 10, 4)
        self.assertEqual(result, 6)

    def test_register_and_execute_multiply(self):
        result = self.handler.execute_command('multiply', 2, 5)
        self.assertEqual(result, 10)

    def test_register_and_execute_divide(self):
        result = self.handler.execute_command('divide', 10, 2)
        self.assertEqual(result, 5)

    def test_execute_unknown_command(self):
        result = self.handler.execute_command('unknown_command', 1, 2)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

