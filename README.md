# monty_python
# 0x19. C - Stacks, Queues - LIFO, FIFO

## The Monty language
Monty 0.98 is a scripting language that is first compiled into Monty byte codes (Just like Python). It relies on a unique stack, with specific instructions to manipulate it. The goal of this project is to create an interpreter for Monty ByteCodes files.
* Implement a monty opcode interpreter in python
---

## Description
A monty opcode interpreter in python

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
## Opcodes list

* push
* pall
* pint
* pop
* swap
* add
* nop
* sub
* div
* mul
* mod
* pchar
* pstr
* rotl
* rotr
* queue
* stack



---

## Author
* **Manuel Torres Vesga** - [matcls](https://github.com/matcls)
