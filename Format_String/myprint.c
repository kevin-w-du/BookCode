#include <stdio.h>
#include <stdarg.h>

int myprint(int Narg, ... )
{
  int i;
  va_list ap;                             

  va_start(ap, Narg);                    
  for(i=0; i<Narg; i++) {
    printf("%d  ", va_arg(ap, int));    
    printf("%f\n", va_arg(ap, double));
  }
  va_end(ap);                         
}

int main() {
  myprint(1, 2, 3.5);                
  myprint(2, 2, 3.5, 3, 4.5);       
  return 1;
}

