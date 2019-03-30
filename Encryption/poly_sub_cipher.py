#!/usr/bin/python3

import random, string

# Generate random mappings
N = 1000
s = "abcdefghijklmnopqrstuvwxyz"
trantab_enc = [None] * N
trantab_dec = [None] * N
for i in range (0, N):
   mapping = random.sample(s, len(s))
   trantab_enc[i] = ''.maketrans(s, ''.join(mapping))
   trantab_dec[i] = ''.maketrans(''.join(mapping), s)

# Encryption
with open('plaintext', 'r') as myfile:
  plaintext = myfile.read()
  ciphertext = [None] * len(plaintext)
  for i in range(0, len(plaintext)):
      ciphertext[i] = plaintext[i].translate(trantab_enc[i % N])
  # Save the ciphertext
  with open('ciphertext', 'w') as cipherfile:
      cipherfile.write(''.join(ciphertext))

# Decryption
with open('ciphertext', 'r') as myfile:
  ciphertext = myfile.read()
  newplaintext = [None] * len(ciphertext)
  for i in range(0, len(ciphertext)):
      newplaintext[i] = ciphertext[i].translate(trantab_dec[i % N])
  print(''.join(newplaintext))

