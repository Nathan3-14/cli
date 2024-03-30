import sys
from typing import Any, Dict, Tuple
from rich.console import Console

class CLI:
    def __init__(self, commands: Dict[str, "Command"]) -> None:
        self.console = Console()
        self.commands = commands

class Command:
    def __init__(self, desired_args: Dict[str, Tuple[Any, Any]]) -> None:
        self.desired_args = desired_args

if __name__ == "__main__":
    add_d_args = {
        "num_1": (float, True),
        "num_2": (float, True)
    }

    commands = {
        "add": Command(add_d_args)
    }
    

    cli = CLI(commands)
