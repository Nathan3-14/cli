import sys
from typing import Any, Dict, List, Tuple
from rich.console import Console

class CLI:
    def __init__(self, commands: Dict[str, "Command"]) -> None:
        self.console = Console()
        self.commands = commands

class Command:
    def __init__(self, desired_args: Dict[str, Tuple[Any, Any]]) -> None:
        self.desired_args = desired_args
        self.desired_args_keys = list(self.desired_args)
    
    def run(self, input_args: List[str]) -> None:
        if not self.check_args(input_args):
            quit()

    def check_args(self, input_args: List[str]) -> bool:
        for index, arg in enumerate(input_args):
            try:
                arg = self.desired_args[
                    self.desired_args_keys[index]
                ][0](arg)
            except ValueError:
                return False
        return True

if __name__ == "__main__":
    add_d_args = {
        "num_1": (float, True),
        "num_2": (float, True)
    }

    commands = {
        "add": Command(add_d_args)
    }
    

    cli = CLI(commands)
