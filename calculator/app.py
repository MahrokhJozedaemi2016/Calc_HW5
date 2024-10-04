# calculator/app.py
from calculator.commands.command_handler import CommandHandler
from calculator.commands.add_command import AddCommand
from calculator.commands.subtract_command import SubtractCommand
from calculator.commands.multiply_command import MultiplyCommand
from calculator.commands.divide_command import DivideCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        # Register the calculator commands
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            if user_input == "exit":
                print("Goodbye!")
                break

            try:
                command_name, *args = user_input.split()
                args = list(map(float, args))  # Convert inputs to float for the calculator
                result = self.command_handler.execute_command(command_name, *args)
                if result is not None:
                    print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception:
                print("Invalid command or arguments.")

