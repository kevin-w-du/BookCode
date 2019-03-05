#include <stdio.h>
#include <arpa/inet.h>
#include <openssl/sha.h>

int main(int argc, const char *argv[])
{
  int i;
  unsigned char buffer[SHA256_DIGEST_LENGTH];
  SHA256_CTX c;

  SHA256_Init(&c);
  for (i =0; i<64; i++)  SHA256_Update(&c, "*", 1);

  c.h[0] = htole32(0x3d848679);    
  c.h[1] = htole32(0x9a77de57);
  c.h[2] = htole32(0x24de2b24);
  c.h[3] = htole32(0xd50d6a24);
  c.h[4] = htole32(0xa7d112d5);
  c.h[5] = htole32(0x8d18c5a5);
  c.h[6] = htole32(0xb6f1295d);
  c.h[7] = htole32(0xbc1481f4);    

  // Append the additional message
  SHA256_Update(&c, "Launch a missile towards the headquarter.", 41);
  SHA256_Final(buffer, &c);
  for (i = 0; i < 32; i++) {
      printf("%02x", buffer[i]);
  }
  printf("\n");

  return 0;
}

