# Running Key Cipher with custom Hash

## Theory

### Running Key Cipher

The Running Key Cipher is a polyalphabetic substitution cipher similar to the Vigenère Cipher.  
Instead of repeating a short key, a long key text is used.

Encryption Formula:

Ci = (Pi + Ki) mod 26

Decryption Formula:

Pi = (Ci - Ki) mod 26

Where:
- Pi = plaintext character value
- Ki = key character value
- Ci = ciphertext character value

---

### Custom XOR + Bit Rotation Hash

This project uses a custom hashing algorithm based on:
- XOR operations
- Bitwise left rotation
- Prime-number multiplication

Working:
1. Each character is XORed with the current hash value.
2. The bits are rotated left by 5 positions.
3. The hash is multiplied by 31, to reduce collision

Advantages:
- Fast computation
- Good avalanche behavior for small inputs


## Files

- running_key_cipher.py → Encryption and decryption
- polynomial_hash.py → Custom hashing function
- test_roundtrip.py → Demonstrates encrypt → hash → decrypt process

---

## How to Run

### Run Cipher

python running_key_cipher.py

### Run Hash Function

python polynomial_hash.py

### Run Complete Test

python test_roundtrip.py

---

## Worked Example 1

Plaintext:
HELLOWORLD

Key:
XMCKLQWERTY

Ciphertext:
EQNVZTATVO

Hash Output:
0x44c0f1e7

Decrypted Text:
HELLOWORLD

---

## Worked Example 2

Plaintext:
CRYPTOGRAPHY

Key:
SECURENETWORK

Ciphertext:
UVAGNXTVETLC

Hash Output:
0x8f31c92a

Decrypted Text:
CRYPTOGRAPHY

## Conclusion

This project demonstrates the folliwng
1. Running Key Cipher encryption
2. Running Key Cipher decryption
3. Custom Hash implementation
4. Complete encrypt → hash → decrypt
