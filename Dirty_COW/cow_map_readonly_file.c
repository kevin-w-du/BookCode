#include <stdio.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[])
{
  char *content="**New content**";
  char buffer[30];
  struct stat st;
  void *map;

  int f=open("/zzz", O_RDONLY);
  fstat(f, &st);
  map=mmap(NULL, st.st_size, PROT_READ, MAP_PRIVATE, f, 0);

  // Open the process's memory pseudo-file
  int fm=open("/proc/self/mem", O_RDWR);                    

  // Start at the 5th byte from the beginning.
  lseek(fm, (off_t) map + 5, SEEK_SET);                     

  // Write to the memory
  write(fm, content, strlen(content));                     

  // Check whether the write is successful
  memcpy(buffer, map, 29);
  printf("Content after write: %s\n", buffer);

  // Check content after madvise
  madvise(map, st.st_size, MADV_DONTNEED);                
  memcpy(buffer, map, 29);
  printf("Content after madvise: %s\n", buffer);

  return 0;
}

