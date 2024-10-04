from calculator.commands.command_handler import BaseCommand

class AddCommand(BaseCommand):
    def execute(self, x, y):
        return x + y
