#!/usr/bin/python3
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

message = b'A secret message*'

# Key generation
key = ECC.generate(curve='P-256')
pem = key.export_key(format='PEM')
open('private_ecc.pem','wb').write(pem.encode())

pub = key.public_key()
pub_pem = pub.export_key(format='PEM')
open('public_ecc.pem','wb').write(pub_pem.encode())

# ECDSA signature generation
key = ECC.import_key(open('private_ecc.pem').read())
h = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(h)


# ECDSA signature verification
key = ECC.import_key(open('public_ecc.pem').read())
h = SHA256.new(message)
verifier = DSS.new(key, 'fips-186-3')
try:
   verifier.verify(h, signature)
   print("The message is authentic.")
except ValueError:
   print("The message is not authentic.")

