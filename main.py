from sys import argv
from os import system

# run compile command
system(f"nasm -f elf64 {argv[1]}.asm -o {argv[1]}.o ")
system(f"ld {argv[1]}.o -o {argv[1]} ")
