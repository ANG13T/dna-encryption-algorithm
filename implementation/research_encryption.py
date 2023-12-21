"""
Python Code Exploring Research Outlined in 
https://hsnarman.github.io/CONF/22-IEMCON-Encryption.pdf

Plain text Message -> ACII Binary -> 2-bit binary encoding rule (base) -> 
Calculate frequencies of each base -> Human coding rule based on frequency (variable length code for each base) -> 
Convert the message into Mbin using variable length code  

P (Plain text) -> M (DNA Bases) -> MBIN variable length code for each base
"""


"""
- DNA Structure
- Nucleotide (Base 4)
- Binary (2 bit encoding)
- Freq
- Huffman Coding to Get Key
- Convert nucleotide bases into cipher
"""

import conversion
import huffman
from collections import Counter

text = "hello"
print("Plain text: " + text)
result_string = conversion.string_to_nucleotide_sequence(text)
print("DNA Bases: " + result_string)
frequencies = Counter(result_string)
print("Frequencies")
print(frequencies)
huffman_codings = huffman.huffman_coding(frequencies)
print("Huffman Codings: ",  huffman_codings)
cipher = conversion.nucleotide_string_to_cipher(result_string, huffman_codings)
print("Cipher: " + cipher)
