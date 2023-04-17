#!/bin/bash

#************************************************************
# Becoming a Certificate Authority (CA)
#************************************************************

# Setup
mkdir -p demoCA && cd demoCA
mkdir -p certs crl newcerts 
rm -f index.txt index.txt.attr serial
touch index.txt index.txt.attr serial
echo "unique_subject = no" > index.txt.attr
echo 1000 > serial
cd ..

mySubject='/CN=www.modelCA.com/O=Model CA LTD./C=US'
# Generate self-signed CA 
openssl req -newkey rsa:4096 -x509 -config config/modelCA_openssl.cnf \
	    -sha256  -days 3650 \
	    -subj "$mySubject"  \
            -keyout modelCA_key.pem -out modelCA_cert.pem  \
	    -passout pass:dees     # Encrypt the private using "dees"


# View the certificate and private key
#openssl x509 -in modelCA.crt -text -noout
#openssl rsa  -in modelCA.key -check -noout -passin pass:dees

