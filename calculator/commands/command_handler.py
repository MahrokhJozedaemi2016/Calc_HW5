from abc import ABC, abstractmethod

class BaseCommand(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, command_name, *args):
        command = self.commands.get(command_name)
        if command:
            return command.execute(*args)
        else:
            print(f"Command '{command_name}' not recognized.")
            return None
