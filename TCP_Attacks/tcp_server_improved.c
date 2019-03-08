#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/ip.h>
#include <arpa/inet.h>

int main()
{
  int sockfd, newsockfd;
  struct sockaddr_in my_addr, client_addr;
  char buffer[100];

  // Step 1: Create a socket
  sockfd = socket(AF_INET, SOCK_STREAM, 0);

  // Step 2: Bind to a port number
  memset(&my_addr, 0, sizeof(struct sockaddr_in));
  my_addr.sin_family = AF_INET;
  my_addr.sin_port = htons(9090);
  bind(sockfd, (struct sockaddr *)&my_addr, sizeof(struct sockaddr_in));

  // Listen for connections
  listen(sockfd, 5);

  int client_len = sizeof(client_addr);
  while (1) {
    newsockfd = accept(sockfd, (struct sockaddr *)&client_addr, &client_len);

    if (fork() == 0) { // The child process           
       close (sockfd);

       // Read data.
       memset(buffer, 0, sizeof(buffer));
       int len = read(newsockfd, buffer, 100);
       printf("Received %d bytes.\n%s\n", len, buffer);

       close (newsockfd);
       return 0;
    } else {  // The parent process                    
       close (newsockfd);
    }
  }

  return 0;
}

