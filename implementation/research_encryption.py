"""
Python Code Exploring Research Outlined in 
https://hsnarman.github.io/CONF/22-IEMCON-Encryption.pdf

Plain text Message -> ACII Binary -> 2-bit binary encoding rule (base) -> 
Calculate frequencies of each base -> Human coding rule based on frequency (variable length code for each base) -> 
Convert the message into Mbin using variable length code  

P (Plain text) -> M (DNA Bases) -> MBIN variable length code for each base
"""

import conversion
import huffman
from collections import Counter

text = "hello"
result_string = conversion.string_to_nucleotide_sequence(text)
print(result_string)
frequencies = Counter(result_string)
print(frequencies)
huffman.huffman_coding(frequencies)

