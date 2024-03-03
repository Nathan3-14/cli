from datetime import datetime
import json
import os
import sys
import re
from typing import Any, Callable, Dict, List

class Main:
    def __init__(self, extra_flags: Dict[str, bool], commands: Dict[str, Callable], help_file_path: str="./help.json"):
        self.args = sys.argv
        self.args.pop(0)

        self.commands = commands
        self.flags = {
        #  "flags_name": False
            "--help": False
        } | extra_flags #? Adds extra flags provided by init

        self.single_flag_regex = r"(?<!-)-[a-zA-Z]{1,}" #? Checks for -a, -ab, -abc etc
        self.word_flag_regex = r"(?<!-)--[a-zA-Z]{1,}" #? Checks for --abc, --defgh etc

        try:
            self.help = json.load(open(help_file_path, "r"))
        except FileNotFoundError:
            self.error([f"No help file called '{help_file_path}'"], "CODE ERR")
        
        # self.main() #! Removed for testing
    

    def main(self):
        self.parse_flags()
        self.check_help()

        self.run_command()



    def run_command(self):
        if not self.args[0].startswith("-"):
            command_to_run = lambda x: x
            if self.args[0] in list(self.commands.keys()):
                command_to_run = self.commands[self.args[0]]
            else:
                self.error([f"No command named '{self.args[0]}'"])
            command_to_run(self.args[1:])


    def error(self, message: List[str], error_prefix: str="ERR", error_log_path: str="./error.log") -> None:
        write_message = f"{datetime.now().strftime('%H:%m:%S')} {message[0]}\n"
        print_message = "\n  ".join(message)

        print(f"  {error_prefix}: {print_message}")

        write_mode = "w"
        if os.path.exists(error_log_path):
            write_mode = "a"
        
        open(error_log_path, write_mode).write(write_message)
        quit()


    def set_flag(self, flags: dict, key: str, value: bool=True):
        if key in list(flags.keys()):
            flags[key] = value
        else:
            self.error([f"No flag with name '{key}'", "Use --help in order to get list of flags"])


    def parse_flags(self):
        for arg in self.args:
            if re.match(self.single_flag_regex, arg) or re.match(self.word_flag_regex, arg): #? Checks if argument given is a flag
                if arg.startswith("--"):
                    self.set_flag(self.flags, f"--{arg[2:]}")
                else: #? Can only be -- or -
                    for char in arg[1:]:
                        self.set_flag(self.flags, f"-{char}")
    

    def check_help(self):
        if self.flags["--help"]:
            self.display_help()
    
    
    def display_help(self):
        for command, command_info in self.help.items():
            print(f"{command.capitalize()}:")
            print(f"  Description: {command_info['description']}")
            print(f"  Usage: {command_info['usage']}")



if __name__ == "__main__":
    def hello(args: List[Any]):
        for name in args:
            print(f"Hello {name}!")

    test = Main({
        "-a": False,
        "-b": False
    }, {
        "hello": hello
    })
    test.main() #! ENABLED FOR TESTING
    
