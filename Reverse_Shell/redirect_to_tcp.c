/* redirect_to_tcp.c */
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>


void main()
{
   struct sockaddr_in server;

   // Create a TCP socket
   int sockfd= socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

   // Fill in the destination information (IP, port #, and family)
   memset (&server, '\0', sizeof(struct sockaddr_in));
   server.sin_family = AF_INET;
   server.sin_addr.s_addr = inet_addr("10.0.2.69");
   server.sin_port   = htons (8080);

   // Connect to the destination
   connect(sockfd, (struct sockaddr*) &server,
           sizeof(struct sockaddr_in));           

   // Send data via the TCP connection
   char *data = "Hello World!";
   // write(sockfd, data, strlen(data));         
   dup2(sockfd, 1);                             
   printf("%s\n", data);                       
}
