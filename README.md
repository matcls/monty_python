# monty_python
# 0x19. C - Stacks, Queues - LIFO, FIFO

## The Monty language
Monty 0.98 is a scripting language that is first compiled into Monty byte codes (Just like Python). It relies on a unique stack, with specific instructions to manipulate it. The goal of this project is to create an interpreter for Monty ByteCodes files.
* Implement a monty opcode interpreter in python
---

## Description
A monty opcode interpreter in python.

## Opcodes list

* push  - Add an element to the stack/queue.
* pall  - Prints all the values int the the stack/queue.
* pint  - Prints the value at the top of the stack/queue.
* pop   - Removes the top element of the stack/queue.
* swap  - Swaps the top two elements of the
* add   - Adds the top two elements of the
* nop   - Desn’t do anything.
* sub   - Subtracts the top element of the
* div   - Divides the second top element of the stack/queue
          by the top element of the stack/queue.
* mul   - Multiply the second top element of the stack/queue
          by the top element of the stack/queue.
* mod   - Computes the rest of the division of the second top element
       of the deque by the top element of the stack/queue.
* pchar - Prints the top element of the stack/queue as a char.
* pstr - Prints the stack/queue as a string starting at the top of the stack/queue
* rotl - Rotates the stack/queue, the top element becomes the last one,
       and the second top element becomes the first one.
* rotr -  Rotates the stack/queue, the last element becomes the top one.
* queue - Sets the format of the data to a queue (FIFO).
* stack - Sets the format of the data to a stack (LIFO)

## Usage
./monty.py file

## Examples

* ./monty bytecodes/pop


## Monty byte code files

Files containing Monty byte codes usually have the .m extension. Most of the industry uses this standard but it is not required by the specification of the language.
There is not more than one instruction per line. There can be any number of spaces before or after the opcode and its argument:
```
pall
  pall
  pall
    push 1 
pall

```

---

## Author
* **Manuel Torres Vesga** - [matcls](https://github.com/matcls)
