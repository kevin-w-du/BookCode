#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int foo(char *str)
{
    char buffer[100];
    unsigned int *framep;

    // Copy ebp into framep
    asm("movl %%ebp, %0" : "=r" (framep));      

    /* print out information for experiment purpose */
    printf("Address of buffer[]:  0x%.8x\n", (unsigned)buffer);
    printf("Frame Pointer value:  0x%.8x\n", (unsigned)framep);

    /* The following statement has a buffer overflow problem */
    strcpy(buffer, str);

    return 1;
}

// For the purpose of experiment
void bar()
{
  static int i = 0;
  printf("The function bar() is invoked %d times!\n", ++i);
}


// For the purpose of experiment
void baz(int x)
{
  printf("The value of baz()'s argument: 0x%.8X\n", x);
}

int main(int argc, char **argv)
{
   char str[2000];
   FILE *badfile;

   char *shell = (char *)getenv("MYSHELL");     
   if(shell){
      printf("The '%s' string's address: 0x%.8x\n", shell,
               (unsigned int)shell);
   }

   badfile = fopen("badfile", "r");
   fread(str, sizeof(char), 2000, badfile);
   foo(str);

   printf("Returned Properly\n");
   return 1;
}


