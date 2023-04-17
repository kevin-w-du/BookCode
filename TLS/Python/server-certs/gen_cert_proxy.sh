#!/bin/bash

fileName="proxy"
#mySubject="/CN=www.example.com"
mySubject="/CN=www.google.com"

# Generate RSA key pair and certificate request 
openssl req -newkey rsa:2048 -batch -sha256 \
            -keyout  ${fileName}_key.pem -out ${fileName}.csr  \
            -subj "$mySubject" \
            -nodes  # no password

# Generate certificate using the CA's certificate
openssl ca -policy policy_anything \
           -md sha256 -days 3650 \
           -in $fileName.csr -out ${fileName}_cert.pem -batch \
           -cert modelCA_cert.pem -keyfile modelCA_key.pem -passin pass:dees



