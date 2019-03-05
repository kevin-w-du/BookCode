#include <stdio.h>
#include <stdlib.h>
#include <openssl/sha.h>
#include <string.h>

void main()
{
  SHA256_CTX ctx;
  u_int8_t results[SHA256_DIGEST_LENGTH];
  int nonce = 0;
  char *msg = "The data in the block";
  char buf[200];
  int len, i;

  while(1) {
    printf("Nonce = %d\n", nonce);
    sprintf(buf, "%d:%s", nonce, msg);
    len = strlen(buf);
    // Compute the SHA256 hash.
    SHA256_Init(&ctx);
    SHA256_Update(&ctx, (u_int8_t *)buf, len);
    SHA256_Final(results, &ctx);
    if (results[0] == 0 && results[1] == 0)
       break;
    else nonce++;
  }

  /* Print the digest as one long hex value */
  for (i = 0; i < SHA256_DIGEST_LENGTH; i++)
       printf("%02x", results[i]);
  putchar('\n');
}
