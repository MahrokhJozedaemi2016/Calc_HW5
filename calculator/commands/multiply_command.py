from calculator.commands.command_handler import BaseCommand

class MultiplyCommand(BaseCommand):
    def execute(self, x, y):
        return x * y
