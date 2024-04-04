from datetime import datetime
import os
from typing import Any, Callable, Dict, List
from rich.console import Console
import yaml

def error(message: str | List[str], console: Console, error_start: str="Err:", error_path: str="logs/errors.log"):
    error_string = f"{datetime.now().strftime("%d/%m/%Y: %H:%M:%S")} - "
    os.makedirs(os.path.dirname(error_path), exist_ok=True)

    console.print(f"  [red]{error_start}[/red] ", end="")
    if isinstance(message, str):
        error_string += message
        console.print(f"{message}")
    elif isinstance(message, list):
        error_string += message[0]
        for index, line in enumerate(message):
            if index == 0:
                console.print(f"{line}")
                continue
            console.print(f"       {line}")
    
    open(error_path, "a").write(f"{error_string}\n")

    quit()

def create_dict_of_commands(file_path: str, command_dict: Dict[str, Callable], console: Console) -> Dict[str, "Command"]: #! # type: ignore
    from .cli import Command
    name_to_command_dict = {
        item["name"]: item
        for item in yaml.load(open(file_path, "r").read(), yaml.BaseLoader)["commands"]
    }

    commands = {}
    for name, command in name_to_command_dict.items():
        commands[name] = Command(command, command_dict[name], console)

    return commands

