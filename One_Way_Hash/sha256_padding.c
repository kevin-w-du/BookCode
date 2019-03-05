#include <stdio.h>
#include <openssl/sha.h>

int main(int argc, const char *argv[])
{
  SHA256_CTX c;
  unsigned char buffer[SHA256_DIGEST_LENGTH];
  int i;

  SHA256_Init(&c);
  SHA256_Update(&c,
    "secretkey:Launch a missile towards Target A."     
    "\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    "\x00\x00\x00\x00\x00\x00\x01\x60"
    "Launch a missile towards the headquarter.",      
    64+41);
  SHA256_Final(buffer, &c);

  for (i = 0; i < 32; i++) {
    printf("%02x", buffer[i]);
  }
  printf("\n");
  return 0;
}
