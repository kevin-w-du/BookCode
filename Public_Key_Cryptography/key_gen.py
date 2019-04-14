#!/usr/bin/python3

from Crypto.PublicKey import RSA

key = RSA.generate(2048)                             
pem = key.export_key(format='PEM', passphrase='dees') 
f = open('private.pem','wb')
f.write(pem)
f.close()

pub = key.publickey()                                  
pub_pem = pub.export_key(format='PEM')
f = open('public.pem','wb')
f.write(pub_pem)
f.close()
