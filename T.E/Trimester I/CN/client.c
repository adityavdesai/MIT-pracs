
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

#define port 8080


int main() {
	int client_sock;
	if((client_sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		printf("socket Failed "); 
        	exit(-1);
	}

	struct sockaddr_in server_addr;
	server_addr.sin_family = AF_INET; 
    	server_addr.sin_port = htons(port);
	server_addr.sin_addr.s_addr = INADDR_ANY;


	int connect_status;
	if((connect_status = connect(client_sock, (struct sockaddr *)&server_addr, sizeof(server_addr))) < 0) {
		printf("socket Failed "); 
        	exit(-1);
	}

	char* message = "Hello, take this data!";
	char  buffer[1024] = {0};

	send(client_sock , message , strlen(message) , 0 ); 
	printf("Hello message sent\n"); 
	int valread = read( client_sock , buffer, 1024); 
	printf("%s\n",buffer );

	return 0;
}
