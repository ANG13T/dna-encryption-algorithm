Nucleotide_Bases = {
    "00": "A",
    "01": "T",
    "10": "G",
    "11": "C"
}

def string_to_nucleotide_sequence(val):
    binary_string = ""
    # create a sequence of bytes put into the encoding of UTF-8
    byte_string = bytearray(val, 'utf-8')
    
    for i in byte_string:
        # appends int to binary string after converting it to binary. This results in 8 bits total and retains the leading 0s via "08b"
        binary_string += str(format(i, '08b'))
    
    print("Binary Representation: ", binary_string)

    binary_bit_list = []

    for i in range(0, len(binary_string), 2):
        binary_bit_list.append(binary_string[i:i+2])

    result_nucleotide_string = ""

    for group in binary_bit_list:
        result_nucleotide_string += Nucleotide_Bases.get(group)

    return result_nucleotide_string

def nucleotide_string_to_cipher(nucleotide_sequence, huffman_codings):
    final_output = ""
    print(huffman_codings)
    for char in nucleotide_sequence:
        final_output += huffman_codings[char]
    print(final_output)
    return final_output

    
def test_string_to_nucleotide():
    text = input("Enter in text input:")
    print("Text Input: ", text)
    output = string_to_nuclotide_sequence(text)
    print("Nucleotide Representation: ", output)
