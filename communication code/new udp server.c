#include &lt;sys/socket.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;arpa/inet.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;err.h&gt;

int main(int argc, char *argv[]) {

	if(argc &lt; 2) { 
//		if(daemon(0,0) == -1) err(1,NULL);
	}

	int sock, n, nr;
	socklen_t fromlen;
	struct sockaddr_in server;
	struct sockaddr_in from;

	sock = socket(AF_INET, SOCK_DGRAM, 0);
	if (sock &lt; 0)
	printf("Can not create socket in server\n");

	memset(&amp;server, 0, sizeof(struct sockaddr_in));
	server.sin_family = AF_INET;
	server.sin_port = htons(5005);
	server.sin_addr.s_addr = INADDR_ANY;

	if(bind(sock, (struct sockaddr *)&amp;server, sizeof(server)) &lt; 0)
	printf("Can not bind in server!\n");
	memset(&amp;from, 0, sizeof(struct sockaddr_in));
	fromlen = sizeof(struct sockaddr_in);


	while(1) {
		int n, l1;
		unsigned char tBuf[300];
		unsigned char outBuf[300];
//		fflush(stdout);

		n = recvfrom(sock, tBuf, 300, 0, (struct sockaddr*) &amp;from, &amp;fromlen);
		if (n &lt; 0) {
			printf("Can not receive in server!\n");
		}

		printf("%s from IP:%s, Port:%hu\r\n",&amp;tBuf[0],inet_ntoa(from.sin_addr), ntohs(from.sin_port));

		strcpy(outBuf,"127 127 0 0\n\0");
		socklen_t length = sizeof(struct sockaddr_in);	
		n = sendto(sock, tBuf, 64, 0, (const struct sockaddr *)&amp;from, fromlen);
		if(n &lt; 0) {
			printf("Can not send from client");
		}

	}
}
