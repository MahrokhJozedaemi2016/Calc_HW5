from calculator.commands.command_handler import BaseCommand

class SubtractCommand(BaseCommand):
    def execute(self, x, y):
        return x - y
