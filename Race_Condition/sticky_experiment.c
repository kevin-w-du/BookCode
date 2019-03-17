#include <stdio.h>
#include <string.h>
#include <errno.h>

int main()
{
   char *fn = "/tmp/XYZ";
   FILE *fp;

   fp = fopen(fn, "r");
   if(fp == NULL) {
      printf("fopen() call failed \n");
      printf("Reason: %s\n", strerror(errno));
   }
   else
     printf("fopen() call succeeded \n");
   fclose(fp);
   return 0;
}

