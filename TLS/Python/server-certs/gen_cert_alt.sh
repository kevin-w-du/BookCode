#!/bin/bash

fileName="mycert2"
mySubject="/CN=www.bank32.com"

# Generate RSA key pair and certificate request 
openssl req -newkey rsa:2048 -batch -sha256  \
            -subj "/CN=www.bank32.com/O=Bank32 Inc./ST=New York/C=US" \
            -addext "subjectAltName = DNS:www.bank32.com,  \
                               DNS:www.bank32A.com, \
                               DNS:www.bank32B.com" \
            -keyout  ${fileName}_key.pem -out $fileName.csr  \
            -passout pass:dees     # Encrypt the private using "dees"


# Generate certificate using the CA's certificate
openssl ca -config ./config/modelCA_openssl.cnf -policy policy_anything \
           -md sha256 -days 3650 \
           -in $fileName.csr -out ${fileName}_cert.pem -batch \
           -cert modelCA_cert.pem -keyfile modelCA_key.pem -passin pass:dees



