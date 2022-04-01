"""Common utilities that can be used by other classes"""
import os


error_msg = "Input not understood"

line = "--------------------"


def clear():
    """Clear the screen to keep things looking nice"""
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")
    else:
        print("Operating system unidentified.  Unable to clear screen.")
