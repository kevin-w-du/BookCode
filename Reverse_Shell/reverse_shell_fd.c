#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <string.h>

void main()
{
  int fd;
  char input[20];
  memset(input, 'a', 20);

  fd = open("/tmp/xyz", O_RDWR);        
  printf("File descriptor: %d\n", fd);
  write(fd, input, 20);                
  close(fd);
}

