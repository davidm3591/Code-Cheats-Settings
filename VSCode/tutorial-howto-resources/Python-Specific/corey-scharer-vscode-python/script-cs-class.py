# Corey Schafer Python for Visual Studio Code
# Available: https://www.youtube.com/watch?v=-nh9rCzPJ20
# Date of video tutorial: 5/1/2020

import sys

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    """Function to greet me."""
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

print(greet('World'))
print(greet('David'))
print("")


# ======================================
# Stopped video at 23:26
print("Stopped video at 23:26")
# ======================================

def print_stuff(stuff_to_print):
    """Print whatever I hand off to it"""
    print(stuff_to_print)

heading = "Class Notes\nTopic and Time"
sep_line = "------------------------------------------------------------------"

vscode_venv = "Creating  a Virtual Environment (venv) at 26:12"
code_formatter = "Installing PEP 8, or Black to format code at 32:17"


print_stuff(sep_line)
print_stuff(heading)
print_stuff(sep_line)

print_stuff(vscode_venv)
print_stuff(code_formatter)

print('')