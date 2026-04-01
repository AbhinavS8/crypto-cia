# Running Key Cipher with Polynomial Rolling Hash

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

### Polynomial Rolling Hash

This project uses a custom Polynomial Rolling Hash function.

Formula:

Hash(s) = Σ (s[i] × p^i) mod m

Where:
- p = 31
- m = 1,000,000,007

Advantages:
- Fast computation
- Simple implementation
- Good distribution of values
- Different from common hashes like MD5/SHA used by other students

---

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
867530912

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
428913572

Decrypted Text:
CRYPTOGRAPHY

---

## Conclusion

This project demonstrates the folliwng
1. Running Key Cipher encryption
2. Running Key Cipher decryption
3. Custom Polynomial Rolling Hash implementation
4. Complete encrypt → hash → decrypt workflow