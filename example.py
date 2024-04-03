from src import CLI, Command, create_dict_of_commands
from rich.console import Console
from typing import Any, List

from src.funcs import create_dict_of_commands


def add(args: List[Any]):
    return args[0] + args[1]

def subtract(args: List[Any]):
    return args[0] - args[1]

def hello(args: List[Any]):
    count = args[1] if len(args) > 1 else 1
    for _ in range(count):
        print(args[0])


console = Console()

command_dict = {
    "add": add,
    "subtract": subtract,
    "hello": hello
}

commands = create_dict_of_commands("./commands.yml", command_dict, console)


cli = CLI(commands, console)

cli.run(input("Enter a command\n>> "), [item for item in input("Enter a list of two numbers, seperated by ', '\n>> ").split(", ")])
