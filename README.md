## Conceptual Understanding

DNA (Deoxyribonucleic acid) is a two stranded genetic molecule consisting of 4 nucleic bases:
- Adenine (A)
- Thymine (T)
- Cytosine (C)
- Guanine (G)

A - T

C - G

DNA mocules have the capacity to store, transmit, and process information by combining its chemical capabilities with classical crytography

Encryption:
plain text -> encryption algorithm (encryption key) -> cipher text

Decryption:
cipher text -> decryption algorithm (encryption key) -> plain text

## Research

https://github.com/nitya123-github/DNA-Genetic-Encryption

## General Workflow

1. Take in input text -> using input
2. Convert the input text into binary 
3. Divide items into bit segments of 2 bit lengths [2 bits turn into one nucleotide]

This project will utilize the UTF-8 encoding.
thie format can translate any Unicode character.
Each ASCII code affilliated with a character in Unicode maps to a byte.
For example:


| Character | ACSCII |   Byte   |
|-----------|--------|----------|
| A         |    065 | 01000001 |
| 9         |    057 | 00111001 |
| ?         |    063 | 00111111 |


The nuclotide bases can be represented using 2 bits
Since 2^2 = 4 with the four possible states being

00 -> A (Adenine)
01 -> G (Guanine)
10 -> C (Cytosine)
11 -> T (Thymine)

Plain text Message -> ACII Binary -> 2-bit binary encoding rule (base) -> Calculate frequencies of each base -> Human coding rule based on frequency (variable length code for each base) -> Convert the message into Mbin using variable length code  

P (Plain text) -> M (DNA Bases) -> MBIN variable length code for each base

# Core Components of an Encryption Algorithm
1. Text Type Support
2. Binary Coding Rule (2-Bit Binary Coding Rule)
3. Encryption Type Specification
4. Encryption Algorithm
5. Data Hiding Algorithm
6. Blind and Not Blind Specification
