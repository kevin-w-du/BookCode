#!/bin/bash

CA='modelCA'
hash=$(openssl x509 -in ../server-certs/${CA}_cert.pem -noout -subject_hash)
ln -s ${CA}_cert.pem $hash.0
