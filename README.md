# CLI
## Contents
- [Usage](#usage)
## Usage
Command yaml file structure:
```yaml
commands:
  - name: <command name>
    description: <command description> !! NOT USED !!
    args:
      - <arg_name_1>: <arg_type_1>
      - <arg_name_2>: <arg_type_2>
      - <arg_name_3>: <arg_type_3>
        required: false !! not needed for required args !!
      [...]
  [...]
```
In order to use the code, download either src (for latest unstable) or dist/cli (for latest stable) and copy it into the root of your project.  
Additionally you can download dist/cli.zip and extract it into the route of your project.
```
|--> main.py
|--> [...]
|--> cli
```
After installing, run `pip install -r cli/requirements.txt`  
In you file you need a rich console created ([more info](https://rich.readthedocs.io/en/stable/reference/console.html)) and you will need to import `CLI` and `create_dict_of_commands` at the top of your file.
```python
#* main.py *#

from rich.console import Console
from cli import CLI, create_dict_of_commands

console = Console()
```
You need to create functions with the following structure, as well as a dictionary containing them all
```python
#* ... *#

def foo(args: List[Any]): #! Type hinting is not nessecary
    # do stuff
    # return values are not nessecary but can be used
def bar(args: List[Any]):
    # do stuff
command_dict = {
    "foo": foo,
    "bar": bar
} #! note the lack of brackets on functions
```
With the dictionary created you need to run the `create_dict_of_commands` function with the path to your yaml file
```python
#* ... *#

commands = create_dict_of_commands("./path-to-file.yml", command_dict, console)
```
Then you need to create the cli object and run commands from it.
```python
#* ... *#

cli = CLI(commands, console)
cli.run("<command>", ["<args>", "<args>"])
```
