import sys
from typing import Any, Dict, List, Tuple, Callable
from rich.console import Console
from rich import print as rprint
from rich import print_json as rprint_json
import json
from funcs import error
from test_funcs import add

print_json = lambda a: rprint_json(json.dumps(a))

class CLI:
    def __init__(self, commands: Dict[str, "Command"]) -> None:
        self.console = Console()
        self.commands = commands

    def run(self, command_name: str, args: List[str]) -> None:
        self.commands[command_name].run(args)

class Command:
    def __init__(self, desired_args: Dict[str, Tuple[Any, Any]], command_function: Callable) -> None:
        self.desired_args = desired_args
        self.desired_args_keys = list(self.desired_args)
        self.command = command_function
    
    def run(self, input_args: List[str]) -> None:
        if not self.check_args(input_args):
            quit()
        rprint(self.command(input_args))
        

    def check_args(self, input_args: List[str]) -> bool:
        for index, arg in enumerate(input_args):
            try:
                input_args[index] = self.desired_args[
                    self.desired_args_keys[index]
                ][0](arg) #? Convert arg to desired type
            except ValueError:
                return False
        return True

if __name__ == "__main__":
    add_d_args = {
        "num_1": (float, True),
        "num_2": (float, True)
    }

    commands = {
        "add": Command(add_d_args, add)
    }
    

    cli = CLI(commands)
    cli.run("add", ["1", "2"])
