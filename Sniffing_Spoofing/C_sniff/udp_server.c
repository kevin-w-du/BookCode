#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/ip.h>

void main()
{
    struct sockaddr_in server;
    struct sockaddr_in client;
    int clientlen;
    char buf[1500];

    // Step (*@\ding{192}@*)
    int sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

    // Step (*@\ding{193}@*)
    memset((char *) &server, 0, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = htonl(INADDR_ANY);
    server.sin_port = htons(9090);

    if (bind(sock, (struct sockaddr *) &server, sizeof(server)) < 0)
        perror("ERROR on binding");

    // Step (*@\ding{194}@*)
    while (1) {
        bzero(buf, 1500);
        recvfrom(sock, buf, 1500-1, 0,
                       (struct sockaddr *) &client, &clientlen);
        printf("%s\n", buf);
    }
    close(sock);
}

