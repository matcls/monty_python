#!/usr/bin/env python3
"""Interpreter for Monty ByteCodes files."""

import os
from sys import argv
import shlex
from opcodes import OPCODES, exit_error


def monty():
    """Start point for monty opcode interpreter."""
    if len(argv) != 2:
        exit_error(1)
    else:
        file = argv[1]
        if os.path.isdir(argv[1]) is False:  # Only for windows
            try:
                with open(file, "r") as monty_file:
                    read(monty_file)
            except FileNotFoundError:
                exit_error(2, None, file)
        else:
            exit_error(0, None, file)


def read(file):
    """Reads the file lines and attemp to execute the instructions
       (one for line).

    Args:
        file (stream): Given file to be interpreted.
    """
    current_line = 0
    for line in file:
        arg_list = shlex.split(line, comments=True)

        def invalid_op(line, *args):
            """Exit the interpreter with an error
             if a instruction is invalid."""
            del args
            exit_error(3, line, arg_list[0])

        def get_op(opcode):
            """Runs the corresponding function for the opcode."""
            OPCODES.get(opcode, invalid_op)(current_line, arg_list)

        current_line += 1

        if arg_list[0:]:  # Ignore blank lines
            get_op(arg_list[0])


if __name__ == '__main__':
    monty()
