from rich.console import Console
from .cli import CLI, Command
from .test_funcs import add

console = Console()

def test():
    add_d_args = {
        "num_1": (float, True),
        "num_2": (float, True),
        "test": (str, False)
    }

    commands = {
        "add": Command(add_d_args, add)
    }
    

    cli = CLI(commands)
    cli.run("add", ["1"])

if __name__ == "__main__":
    test()
