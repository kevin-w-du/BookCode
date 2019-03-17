#include <sys/mman.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <string.h>

int main()
{
  struct stat st;
  char content[20];
  char *new_content = "New Content";
  void *map;

  int f=open("./zzz", O_RDWR);                      
  fstat(f, &st);
  // Map the entire file to memory
  map=mmap(NULL, st.st_size, PROT_READ|PROT_WRITE, 
                             MAP_SHARED, f, 0);

  // Read 10 bytes from the file via the mapped memory
  memcpy((void*)content, map, 10);                
  printf("read: %s\n", content);

  // Write to the file via the mapped memory
  memcpy(map+5, new_content, strlen(new_content)); 

  // Clean up
  munmap(map, st.st_size);
  close(f);
  return 0;
}

