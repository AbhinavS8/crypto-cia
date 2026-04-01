# Custom Polynomial Rolling Hash Function
# Author: Your Name

MOD = 1000000007
BASE = 31


def polynomial_hash(text):
    hash_value = 0
    power = 1

    for char in text:
        hash_value = (hash_value + (ord(char) * power)) % MOD
        power = (power * BASE) % MOD

    return hash_value


if __name__ == "__main__":
    text = input("Enter text to hash: ")
    print("Hash Value:", polynomial_hash(text))