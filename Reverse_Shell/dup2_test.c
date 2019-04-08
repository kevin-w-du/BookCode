#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>

void main()
{
  int fd0, fd1;
  char input[100];
  fd0 = open("/tmp/input",  O_RDONLY);
  fd1 = open("/tmp/output", O_RDWR);
  printf("File descriptors: %d, %d\n", fd0, fd1);
  dup2(fd0, 0);                       
  dup2(fd1, 1);                      
  scanf("%s",  input);              
  printf("%s\n", input);           
  close(fd0); close(fd1);
}

