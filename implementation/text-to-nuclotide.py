Nucleotide_Bases = {
    "00": "A",
    "01": "G",
    "10": "C",
    "11": "T"
}

resultant = []

def string_to_nuclotide_sequence(val):
    binary_string = ""
    # create a sequence of bytes put into the encoding of UTF-8
    byte_string = bytearray(val, 'utf-8')
    print("h", byte_string)
    for i in byte_string:
        # appends int to binary string after converting it to binary. This results in 8 bits total and retains the leading 0s via "08b"
        print(format(i, '08b'))
        binary_string += str(format(i, '08b'))
    print("hi", binary_string)

    binary_bit_list = []

    for i in range(0, len(binary_string), 2):
        binary_bit_list.append(binary_string[i:i+2])

    print(binary_bit_list)

    

text = input("Enter in text input:")
string_to_nuclotide_sequence(text)

