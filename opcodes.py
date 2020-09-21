#!/usr/bin/env python3
"""Implement the opcode functions.

Attributes:
    QUEUE (bool): The current state of the interpreter (LIFO or FIFO).
    SQ (collections.deque): doble ended queue object.
"""
from sys import stderr, exit as exit_
from collections import deque

SQ = deque()
QUEUE = False


def op_push(line, *arg):
    """Add an element to the deque."""
    # handle integers
    try:
        int(arg[0][1])
    except (ValueError, TypeError, IndexError):
        exit_error(4, line)
    num = int(arg[0][1])
    if QUEUE is False:
        SQ.append(num)
    else:
        SQ.appendleft(num)


def op_pall(*arg):
    """prints all the values on the deque"""
    del arg
    if SQ:
        sqr = reversed(SQ)
        for elem in sqr:
            print(elem)


def op_pint(line, *arg):
    """ prints the value at the top of the deque"""
    del arg
    if SQ:
        print(SQ[-1])
    else:
        exit_error(5, line)


def op_pop(line, *arg):
    """removes the top element of the deque"""
    del arg
    try:
        if QUEUE is False:
            SQ.popleft()
        else:
            SQ.pop()
    except IndexError:
        exit_error(6, line)


def op_swap(line, *arg):
    """swaps the top two elements of the deque"""
    del arg
    try:
        last = SQ.pop()
        newlast = SQ.pop()
        SQ.append(last)
        SQ.append(newlast)
    except IndexError:
        exit_error(7, line)


def op_add(line, *arg):
    """adds the top two elements of the deque"""
    del arg
    try:
        add = (SQ[-1] + SQ[-2])
        SQ.pop()
        SQ.pop()
        SQ.append(add)
    except IndexError:
        exit_error(8, line)


def op_nop(line, *arg):
    """doesn’t do anything"""
    del arg, line


def op_sub(line, *arg):
    """subtracts the top element of the deque
       from the second top element of the deque"""
    del arg
    try:
        sub = (SQ[-2] - SQ[-1])
        SQ.pop()
        SQ.pop()
        SQ.append(sub)
    except IndexError:
        exit_error(9, line)


def op_div(line, *arg):
    """divides the second top element of the deque
       by the top element of the deque"""
    del arg
    try:
        div = (SQ[-2] // SQ[-1])
        SQ.pop()
        SQ.pop()
        SQ.append(div)
    except ZeroDivisionError:
        exit_error(10, line)
    except IndexError:
        exit_error(11, line)


def op_mul(line, *arg):
    """multiplies the second top element of the deque
       with the top element of the deque"""
    del arg
    try:
        mul = (SQ[-2] * SQ[-1])
        SQ.pop()
        SQ.pop()
        SQ.append(mul)
    except IndexError:
        exit_error(12, line)


def op_mod(line, *arg):
    """computes the rest of the division of the second top element
       of the deque by the top element of the deque"""
    del arg
    try:
        div = (SQ[-2] % SQ[-1])
        SQ.pop()
        SQ.pop()
        SQ.append(div)
    except ZeroDivisionError:
        exit_error(13, line)
    except IndexError:
        exit_error(14, line)


def op_pchar(line, *arg):
    """ prints the char at the top of the deque"""
    # if 65 <= SQ[-1] <= 90 or 97 <= SQ[-1] <=122:
    del line, arg
    if 0 <= SQ[-1] <= 127:
        print(chr(SQ[-1]))


def op_pstr(line, *arg):
    """ prints the string starting at the top of the deque"""
    del line, arg
    if SQ:
        SQ.reverse()
        for i in SQ:
            if i == 0:
                print()
                break
            if 65 <= i <= 97 or 90 <= i <= 122:
                print(chr(i), end="")
            else:
                print()
                break
    else:
        print()


def op_rotl(line, *arg):
    """rotates the deque, the top element becomes the last one,
       and the second top element becomes the first one"""
    del arg, line
    SQ.rotate(1)


def op_rotr(line, *arg):
    """rotates the deque, the last element becomes the top one."""
    del arg, line
    SQ.rotate(-1)


def op_queue(line, *arg):
    """sets the format of the data to a queue (FIFO)"""
    del arg, line
    global QUEUE, SQ
    if QUEUE is False:
        QUEUE = True
        # SQ.reverse()


def op_stack(line, *arg):
    """sets the format of the data to a stack (LIFO)"""
    del arg, line
    global QUEUE, SQ
    if QUEUE is True:
        # SQ.reverse()
        QUEUE = False


def exit_error(error=0, line=None, file=None):
    """Exits the interreter with a error state."""
    if error == 0:
        print(file, "is a directory \nUSAGE: monty file", file=stderr)
    if error == 1:
        print("USAGE: monty file", file=stderr)
    if error == 2:
        print("Error: Can't open file", file)
    if error == 3:
        print("L" + str(line) + ": unknown instruction", file, file=stderr)
    if error == 4:
        print("L" + str(line) + ": usage: push integer", file=stderr)
    if error == 5:
        print("L" + str(line) + ": can't pint, stack empty", file=stderr)
    if error == 6:
        print("L" + str(line) + ": can't pop an empty stack", file=stderr)
    if error == 7:
        print("L" + str(line) + ": can't swap, stack too short", file=stderr)
    if error == 8:
        print("L" + str(line) + ": can't add, stack too short", file=stderr)
    if error == 9:
        print("L" + str(line) + ": can't sub, stack too short", file=stderr)
    if error == 10:
        print("L" + str(line) + ": division by zero", file=stderr)
    if error == 11:
        print("L" + str(line) + ": can't div, stack too short", file=stderr)
    if error == 12:
        print("L" + str(line) + ": can't mul, stack too short", file=stderr)
    if error == 13:
        print("L" + str(line) + ": division by zero", file=stderr)
    if error == 14:
        print("L" + str(line) + ": can't mod, stack too short", file=stderr)
    exit_(1)


OPCODES = {
    "push": op_push,
    "pall": op_pall,
    "pint": op_pint,
    "pop": op_pop,
    "swap": op_swap,
    "add": op_add,
    "nop": op_nop,
    "sub": op_sub,
    "div": op_div,
    "mul": op_mul,
    "mod": op_mod,
    "pchar": op_pchar,
    "pstr": op_pstr,
    "rotl": op_rotl,
    "rotr": op_rotr,
    "queue": op_queue,
    "stack": op_stack
}
