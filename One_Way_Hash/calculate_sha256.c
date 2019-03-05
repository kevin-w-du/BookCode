#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

void main()
{
  SHA256_CTX ctx;
  u_int8_t results[SHA256_DIGEST_LENGTH];
  int i;
  char *msg_part1 = "Part One ";
  char *msg_part2 = "Part Two ";
  char *msg_part3 = "Part Three";


  SHA256_Init(&ctx);             
  SHA256_Update(&ctx, msg_part1, strlen(msg_part1)); 
  SHA256_Update(&ctx, msg_part2, strlen(msg_part2));
  SHA256_Update(&ctx, msg_part3, strlen(msg_part3)); 
  SHA256_Final(results, &ctx);   

  /* Print the message and the hash */
  printf("%s%s%s\n", msg_part1, msg_part2, msg_part3);
  for (i = 0; i < SHA256_DIGEST_LENGTH; i++)
       printf("%02x", results[i]);
  printf("\n");
}

