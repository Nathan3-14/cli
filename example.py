from src import CLI, Command
from rich.console import Console
from typing import List


def add(args: List[float]):
    return args[0] + args[1]

def subtract(args: List[float]):
    return args[0] - args[1]


console = Console()

commands = {
    "add": Command(
        {
            "name": "add",
            "args": [
                {"num_1": "float"},
                {"num_2": "float"}
            ]
        },
        add,
        console
    ),
    "subtract": Command(
        {
            "name": "subtract",
            "args": [
                {"num_1": "float"},
                {"num_2": "float"}
            ]
        },
        subtract,
        console
    )
}

command_dict = {
    "add": add,
    "subtract": subtract
}

cli = CLI(commands, console, "./commands.yml")

cli.run(input("Enter a command\n>> "), [item for item in input("Enter a list of two numbers, seperated by ', '\n>> ").split(", ")])
