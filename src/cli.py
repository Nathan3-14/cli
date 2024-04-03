from typing import Any, Dict, List, Tuple, Callable
from rich.console import Console
from rich import print as rprint
from rich import print_json as rprint_json
import json

import yaml
from .funcs import error

print_json = lambda a: rprint_json(json.dumps(a))

class CLI:
    def __init__(self, commands: Dict[str, "Command"], command_list: List[Callable], console: Console, command_file: str) -> None:
        self.console = console
        self.commands = commands
        self.command_list = command_list

    def run(self, command_name: str, args: List[str]) -> None:
        self.commands[command_name].run(args)

class Command:
    def __init__(self, desired_args: Dict[str, Any], command_function: Callable, console: Console) -> None: #! Type should be Tuple[Any, bool] but bool doesn't work
        self.console = console

        self.command = command_function

        self.desired_args = self.convert_command_dict(desired_args)
        self.desired_args_keys = list(self.desired_args)

        expected_arg_types = [f"{'<' if arg_type[1] else '['}[blue bold]{arg_name}[/blue bold]: [dark_blue bold]{arg_type[0].__name__}[/dark_blue bold]{'>' if arg_type[1] else ']'}" for arg_name, arg_type in self.desired_args.items()]
        self.expected_arg_string = f"[medium_spring_green]main.py {' '.join(expected_arg_types)}[/medium_spring_green]"
    
    def run(self, input_args: List[str]) -> None:
        if not self.check_args(input_args):
            recieved_args_in = [f"{arg}" for arg in input_args]
            self.recieved_args_string = f"[medium_spring_green]main.py {' '.join(recieved_args_in)}[/medium_spring_green]"
            error([
                f"Incorrect argument supplied",
                f"Expected {self.expected_arg_string}",
                f"but recieved {self.recieved_args_string}"
            ], self.console)
            quit()
        output = self.command(input_args)
        if output != None:
            self.console.print(self.command(input_args))
        

    def convert_command_dict(self, command_dict: Dict[str, Any]) -> Dict[str, Tuple[Any, Any]]:
        type_conversion = {
            "int": int,
            "str": str,
            "float": float
        }

        desired_args = {}

        command_args = command_dict["args"]

        for argument in command_args:
            argument_keys = list(argument.keys())
            argument_name = argument_keys[0]
            try:
                argument_type = type_conversion[argument[argument_name]]
            except KeyError:
                error(f"Type {argument[argument_name]} is not recognised", self.console)
            
            argument_required = True if "required" not in argument_keys else ( False if argument["required"] == "false" else True )

            desired_args[argument_name] = (argument_type, argument_required)

        return desired_args


    def check_args(self, input_args: List[str]) -> bool:
        for index, (arg_name, arg_data) in enumerate(self.desired_args.items()):
            try:
                input_args[index] = arg_data[0](input_args[index]) #? Convert arg to desired type
            except ValueError:
                print("value error")
                return False
            except IndexError:
                if arg_data[1]:
                    return False
        return True

    def __str__(self) -> str:
        return f"{self.desired_args}"


