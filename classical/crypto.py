ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# XOR / One Time Padding Implemnentation (aka Vernam Cipher)
def vernam_cipher_encrypt(plain, key):
    if len(plain) != len(key):
        print("Unable to conduct Vernam cipher! They must be same length!")
        return
    plain = plain.upper()
    key = key.upper()

    for index in len(plain):
        val_1 = str(bin(ALPHABET.index(plain[i])))
        val_2 = str(bin(ALPHABET.index(key[i]))
        xor = XOR(val_1, val_2)

def XOR(val_1, val_2):
    result = ""
    for i in len(val_1):
        v_1 = int(val_1[i])
        v_2 = int(val_2[i])
        if (v_1 == v_2):
            result.concat("0")
        else:
            result.concat("1")

    return result



def vernam_cipher_decrypt(cipher, key):
    if len(cipher) != len(key):
        print("Unable to conduct Vernam cipher! They must be same length!")
        return

    plain = plain.upper()
    key = key.upper()

    f


"""
Steps:
1. Convert the Plain Text and Key into Numerical Formats (A = 0, B = 1, C = 2)
2. As each character is put into the numerical format, get the binary representation of the decimal
3. Do XOR for each character binary representation in the plain text and the key
4. If the resultant XOR is greater than 26 (# of letters in the alphabet, subtract 26). This will give you the cipher text
ne Time Pad Algorithm
5. Decryption is the reverse process of encryption
"""









