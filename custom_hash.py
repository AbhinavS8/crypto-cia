# Custom XOR + Bit Rotation Hash Function
# Author: Your Name

def rotate_left(value, shift, bits=32):
    return ((value << shift) & (2**bits - 1)) | (value >> (bits - shift))


def custom_hash(text):
    hash_value = 0xABCDEF12

    for char in text:
        hash_value ^= ord(char)
        hash_value = rotate_left(hash_value, 5)
        hash_value = (hash_value * 31) & 0xFFFFFFFF

    return hex(hash_value)


if __name__ == "__main__":
    text = input("Enter text to hash: ")
    print("Hash Value:", custom_hash(text))