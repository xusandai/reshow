#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <sys/un.h>
#include <unistd.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <arpa/inet.h>
using namespace std;
int main()
{
	int sockfd;
	int len;
	struct sockaddr_in address;
	int result;
	unsigned char ch;
  	sockfd=socket(AF_INET,SOCK_STREAM,0);
	address.sin_family=AF_INET;
	address.sin_addr.s_addr=inet_addr("127.0.0.1");
	address.sin_port=htons(12345);
 	len=sizeof(address);
	result=connect(sockfd,(struct sockaddr * ) &address, len);
	
	//read the the logon message
	FILE * file=fopen("../test/sz_2016_11_01.txt","rb");    
 	char logon_msg[104];
    size_t n=fread(logon_msg,104,1,file);    
    //printf("%d   %x\n",n,logon_msg[3]);

	if(result==-1)
	{
		perror("oops:client!");
		exit(1);
	}
	printf("connect success");

	write(sockfd,logon_msg,104);
	int i=500;
	while(i--)		
	{	
		read(sockfd,&ch,1);
		printf("%02x ",ch);
	}
	close(sockfd);
exit(0);
}
