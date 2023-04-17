#include <unistd.h>
#include <arpa/inet.h>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <netdb.h>

#define CHK_SSL(err) if ((err) < 1) { ERR_print_errors_fp(stderr); exit(2); }
#define CHK_ERR(err,s) if ((err)==-1) { perror(s); exit(1); }

void processRequest(SSL* ssl, int sock)
{
    char buf[1024];
    int len = SSL_read (ssl, buf, sizeof(buf) - 1);
    buf[len] = '\0';
    printf("Received: %s\n",buf);

    // Construct and send the HTML page
    char *html =
      "HTTP/1.1 200 OK\r\n"                        
      "Content-Type: text/html\r\n\r\n"
      "<!DOCTYPE html><html>"
      "<head><title>Hello World</title>"
      "<style>body {background-color: black}"
      "h1 {font-size:3cm; text-align: center; color: white;"
      "text-shadow: 0 0 3mm yellow}</style></head>"
      "<body><h1>Hello, world!</h1></body></html>"; 
    SSL_write(ssl, html, strlen(html));
    SSL_shutdown(ssl);  SSL_free(ssl);
}



int setupTCPServer()
{
    struct sockaddr_in sa_server;
    int listen_sock, err, tr = 1;

    // Create a listening socket
    listen_sock= socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    err = setsockopt(listen_sock, SOL_SOCKET, SO_REUSEADDR,
                     &tr, sizeof(int));
    CHK_ERR(err, "setsockopt");

    // Prepare for address structure
    memset (&sa_server, '\0', sizeof(sa_server));
    sa_server.sin_family      = AF_INET;
    sa_server.sin_addr.s_addr = INADDR_ANY;
    sa_server.sin_port        = htons (4433);

    // Bind the socket to a port
    err = bind(listen_sock, (struct sockaddr*)&sa_server,
                                 sizeof(sa_server));
    CHK_ERR(err, "bind");

    // Listen to connections
    err = listen(listen_sock, 5);
    CHK_ERR(err, "listen");
    return listen_sock;
}

int main()
{
  const SSL_METHOD *meth;
  SSL_CTX* ctx;
  SSL* ssl;

  // Step 0: OpenSSL library initialization
  SSL_library_init();
  SSL_load_error_strings();

  // Step 1: SSL context initialization
  meth = (SSL_METHOD *)TLSv1_2_method();
  ctx = SSL_CTX_new(meth);
  SSL_CTX_set_verify(ctx, SSL_VERIFY_NONE, NULL);

  // Step 2: Set up the server certificate and private key
  SSL_CTX_use_certificate_file(ctx, "./cert_server/bank32_cert.pem",
                                SSL_FILETYPE_PEM);
  /* SSL_CTX_use_certificate_chain_file(ctx, ...); */
  SSL_CTX_use_PrivateKey_file(ctx, "./cert_server/bank32_key.pem",
                                SSL_FILETYPE_PEM);

  // Step 3: Create a new SSL structure for a connection
  ssl = SSL_new (ctx);

  struct sockaddr_in sa_client;
  size_t client_len;

  int listen_sock = setupTCPServer();
  while (1) {
    int sock = accept(listen_sock, (struct sockaddr*)&sa_client, &client_len);
    printf ("TCP connection established!\n");
    if (fork() == 0) { // Child process
       close (listen_sock);

       SSL_set_fd (ssl, sock);
       int err = SSL_accept (ssl);
       CHK_SSL(err);
       printf ("SSL connection established!\n");

       processRequest(ssl, sock);
       close(sock);
       return 0;
    } else { // Parent process
        close(sock);
    }
  }
}
