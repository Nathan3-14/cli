from src import CLI, Command
from rich.console import Console
from typing import List


def add(args: List[float]):
    return args[0] + args[1]

def subtract(args: List[float]):
    return args[0] - args[1]


console = Console()

command_dict = {
    "add": add,
    "subtract": subtract
}

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
for command in "command list":
    create command dict as above using commands.yml

#TODO maybe make a function that auto generates commands?

cli = CLI(commands, console)

cli.run(input("Enter a command\n>> "), [item for item in input("Enter a list of two numbers, seperated by ', '\n>> ").split(", ")])
