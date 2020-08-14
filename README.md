# Ciphers

A python implementation of 3 Ciphers. Includes a console menu for encoding and decoding.

## Encrypt

1. Ceasar: The cipher asks for a message and a letter to use, returning the encrypted text.
2. Vigenere: The cipher ask for a message and a key, returning the ciphertext.
3. One time pad: The cipher aks for a message and return a key and the ciphertext. The key is generated randomly.

## Decrypt
4. Decrypts the file cipher1.txt. This uses a cesar cipher. It can be decrypted with a brute force attack or a frequency analysis. The decrypted text is stored in cipher1_decrypted.text
5. Decrypt the file cipher2.txt. It uses valid 4-letter key encryption. It does not use letter statistics as most do, but an iterative frecuency analysis.

## Usage 
`python3 ciphers.py`