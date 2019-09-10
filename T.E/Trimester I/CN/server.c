
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

#define port 8080

int main() {
	struct sockaddr_in client_address;

	int server_sock;
	if((server_sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		printf("Socket Failed "); 
        	exit(-1);
	}

	client_address.sin_family = AF_INET;
	client_address.sin_port = htons(port); 
	client_address.sin_addr.s_addr = INADDR_ANY;
	
	if (bind(server_sock, (struct sockaddr *)&client_address, sizeof(client_address)) < 0) 
    	{ 
       		printf("Bind Failed "); 
      	 	exit(-1); 
    	} 


	if (listen(server_sock, 1) < 0) 
	{ 
		printf("Listen failed "); 
		exit(-1); 
	}

	
	int accept_socket;
	int addrlen = sizeof(client_address);
	if ((accept_socket = accept(server_sock, (struct sockaddr *)&client_address, (socklen_t*)&addrlen)) < 0) 
    	{ 
		printf("Accept failed "); 
		exit(-1); 
    	}

	char buffer[1024] = {0};
	int valread = read( accept_socket , buffer, 1024);
	printf("%s", buffer);

	char* message = "\n Message Received !!\n";
	send(accept_socket , message , strlen(message) , 0 ); 
    	printf("\n Acknowledgement message sent!\n");

	return 0;
}

