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

        self.run_command()



    def run_command(self):
        flags = []
        for arg in self.args.copy():
            if arg.startswith("-"):
                flags.append(arg)
                self.args.remove(arg)
            else:
                if arg in list(self.commands.keys()):
                    command_to_run = self.commands[arg]
                    break
                else:
                    self.error([f"No command named '{arg}'"])
        
        print(f"Running '{self.args[0]}' with {self.args[1:]}")
        command_to_run(self.args[1:], flags)


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
            if re.match(self.word_flag_regex, arg): #? Checks if argument given is a flag
                self.set_flag(self.flags, f"--{arg[2:]}")
    

    
    def display_help(self):
        for command, command_info in self.help.items():
            print(f"{command.capitalize()}:")
            print(f"  Description: {command_info['description']}")
            print(f"  Usage: {command_info['usage']}")

def check_flag(flag: str, flags: List[str]):
    return flag in flags



if __name__ == "__main__":
    def hello(args: List[Any], flags: List[str]):
        for name in args:
            print(f"Hello {name}!", end=" " if check_flag("-o", flags) else "\n")
        
        if check_flag("-o", flags):
            print("")
    

    
    test = Main({}, {
        "hello": hello
    })
    test.main() #! ENABLED FOR TESTING
    
