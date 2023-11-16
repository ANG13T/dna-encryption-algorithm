ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# XOR / One Time Padding Implemnentation (aka Vernam Cipher)
def vernam_cipher_encrypt(plain, key):
    if len(plain) != len(key):
        print("Unable to conduct Vernam cipher! They must be same length!")
        return
    plain = plain.upper()
    key = key.upper()
    output = ""

    for index in range(len(plain)):
        val_1 = str(bin(ALPHABET.index(plain[index])))[2:]
        val_2 = str(bin(ALPHABET.index(key[index])))[2:]
        bin_length = len(val_2)
        if len(val_1) > len(val_2):
            bin_length = len(val_1)
        val_1 = val_1.zfill(bin_length)
        val_2 = val_2.zfill(bin_length)
        xor = int(XOR(val_1, val_2), 2)
        if xor >= 26:
            xor -= 26
        output += ALPHABET[xor]

    print("CIPHER: " + output)


def XOR(val_1, val_2):
    result = ""
    for i in range(len(val_1)):
        v_1 = int(val_1[i])
        v_2 = int(val_2[i])
        print("-", v_1, v_2)
        if (v_1 == v_2):
            result += "0"
        else:
            result += "1"

    return result

def RXOR(val_1, val_2):
    result = ""
    print(val_1, val_2)
    for i in range(len(val_1)):
        v_1 = int(val_1[i])
        v_2 = int(val_2[i])

        if (v_1 == "0"):
            result += val_2[i]
        else:
            if v_2 == "1":
                result += "0"
            else:
                result += "1"

    return result


def vernam_cipher_decrypt(cipher, key):
    if len(cipher) != len(key):
        print("Unable to conduct Vernam cipher! They must be same length!")
        return

    cipher = cipher.upper()
    key = key.upper()
    output = ""

    for index in range(len(cipher)):
        alpha_1 = ALPHABET.index(cipher[index])
        alpha_2 = ALPHABET.index(key[index])
        if alpha_1 < alpha_2:
            alpha_1 += 26

        val_1 = str(bin(alpha_1))[2:]
        val_2 = str(bin(alpha_2))[2:]
        print("values", val_1, val_2, cipher[index], key[index])

        bin_length = len(val_2)
        if len(val_1) > len(val_2):
            bin_length = len(val_1)

        val_1 = val_1.zfill(bin_length)
        val_2 = val_2.zfill(bin_length)
        print("values", val_1, val_2, cipher[index], key[index])

        rxor = RXOR(val_1, val_2)

        print(rxor)

        # return
        outcome = int(rxor, 2)
        if outcome > 26:
            outcome = outcome - 26
        print(outcome)
        output += ALPHABET[outcome]

    print("Plain Text: " + output)

def implement_dna_sequence():
    # this function is used to impart the DNA sequence
    return


vernam_cipher_encrypt("OAK", "SON")
vernam_cipher_decrypt("COH", "SON")


"""
Steps:
1. Convert the Plain Text and Key into Numerical Formats (A = 0, B = 1, C = 2)
2. As each character is put into the numerical format, get the binary representation of the decimal
3. Do XOR for each character binary representation in the plain text and the key
4. If the resultant XOR is greater than 26 (# of letters in the alphabet, subtract 26). This will give you the cipher text
ne Time Pad Algorithm
5. Decryption is the reverse process of encryption
"""
