#!/bin/bash

# Assembling with Nasm
nasm -f elf32 -o $1.o $1.nasm


# Linking object
ld -o $1 $1.o
echo ' '
echo '____Done___'
echo ' '