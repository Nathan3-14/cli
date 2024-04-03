from datetime import datetime
import os
from typing import List
from rich.console import Console

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