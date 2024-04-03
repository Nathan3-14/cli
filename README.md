# CLI
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
In order to use the code, download either src or dist/cli and copy it into the root of your project.
```
|--> main.py
|--> [...]
|--> cli
```
After installing, run `pip install -r cli/requirements.txt`  
In you file you need a rich console created ([more info](https://rich.readthedocs.io/en/stable/reference/console.html))  
You will need to import `CLI` and `create_dict_of_commands`
```python
#* main.py *#
from rich.console import Console
from cli import CLI, create_dict_of_commands

console = Console()
```
You need to create functions with the following structure.
```python
def foo(args: List[Any]): #! Type hinting is not nessecary
```