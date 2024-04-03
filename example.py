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
        {"num_1": (float, True), "num_2": (float, True)},
        add,
        console
    ),
    "subtract": Command(
        {"num_1": (float, True), "num_2": (float, True)},
        subtract,
        console
    )
}

cli = CLI(commands, console)

cli.run(input("Enter a command\n>> "), [item for item in input("Enter a list of two numbers, seperated by ', '\n>> ").split(", ")])
