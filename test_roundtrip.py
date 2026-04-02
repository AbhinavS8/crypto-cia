from running_key_cipher import encrypt, decrypt
from custom_hash import custom_hash

plaintext = "HELLOWORLD"
key = "XMCKLQWERTY"

print("Original Plaintext:", plaintext)

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

hash_output = custom_hash(ciphertext)
print("Hash of Ciphertext:", hash_output)

decrypted = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted)

if decrypted == plaintext:
    print("Round-trip successful!")
else:
    print("Round-trip failed!")