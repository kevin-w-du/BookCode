#include <arpa/inet.h>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <netdb.h>

#define CHK_SSL(err) if ((err) < 1) { ERR_print_errors_fp(stderr); exit(2); }

SSL* setupTLSClient(const char* hostname)
{
   // Step 0: OpenSSL library initialization
   // This step is no longer needed as of version 1.1.0.
   SSL_library_init();
   SSL_load_error_strings();

   // Step 1: SSL context initialization
   SSL_METHOD *meth = (SSL_METHOD *)TLSv1_2_method();
   SSL_CTX* ctx = SSL_CTX_new(meth);
   SSL_CTX_set_verify(ctx, SSL_VERIFY_PEER, NULL);
   SSL_CTX_load_verify_locations(ctx, NULL, "./cert");

   // Step 2: Create a new SSL structure for a connection
   SSL* ssl = SSL_new (ctx);

   // Step 3: Enable the hostname check
   X509_VERIFY_PARAM *vpm = SSL_get0_param(ssl);
   X509_VERIFY_PARAM_set1_host(vpm, hostname, 0);

   return ssl;
}

int setupTCPClient(const char* hostname, int port)
{
   struct sockaddr_in server_addr;

   // Get the IP address from hostname
   struct hostent* hp = gethostbyname(hostname);

   // Create a TCP socket
   int sockfd= socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

   // Fill in the destination information (IP, port #, and family)
   memset (&server_addr, '\0', sizeof(server_addr));
   memcpy(&(server_addr.sin_addr.s_addr), hp->h_addr, hp->h_length);
   server_addr.sin_port   = htons (port);
   server_addr.sin_family = AF_INET;

   // Connect to the destination
   connect(sockfd, (struct sockaddr*) &server_addr,
           sizeof(server_addr));

   return sockfd;
}


int main(int argc, char *argv[])
{
   char *hostname = "example.com";
   int port = 443;

   if (argc > 1) hostname = argv[1];
   if (argc > 2) port = atoi(argv[2]);

   // TLS initialization and create TCP connection
   SSL *ssl   = setupTLSClient(hostname);
   int sockfd = setupTCPClient(hostname, port);

   // TLS handshake
   SSL_set_fd(ssl, sockfd);
   int err = SSL_connect(ssl); CHK_SSL(err);
   printf("SSL connection is successful\n");
   printf ("SSL connection using %s\n", SSL_get_cipher(ssl));

   // Send and Receive data
   char buf[9000];
   char sendBuf[200];

   sprintf(sendBuf, "GET / HTTP/1.1\nHost: %s\n\n", hostname);
   SSL_write(ssl, sendBuf, strlen(sendBuf));

   int len;
   do {
     len = SSL_read (ssl, buf, sizeof(buf) - 1);
     buf[len] = '\0';
     printf("%s\n",buf);
   } while (len > 0);
}


