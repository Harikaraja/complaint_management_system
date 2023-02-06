#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
void divisor(int div[100],int rem[100],int s);
void detection(int s,int divide[100]);
void main()
{
	int i,data[100],n,div_bit,div[100],rem[100],size;
	printf("Enter the size of the data : ");
	scanf("%d",&n);
	printf("Enter the data : ");
	for(i=0;i<n;i++)
	scanf("%d",&data[i]);
	div_bit=17;
	int divide[17]={1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1};
	size=div_bit-1;
	for(i=0;i<size;i++)
	div[i]=data[i];
	for(i=0;i<(n+size);i++)
	rem[i]=div[i];
	divisor(divide,rem,size);
	detection(size,divide);
}
void divisor(int div[100],int rem[100],int size)
{
	int cur=0,i,crc[100];
	while(1)
	{
		for(i=0;i<size;i++)
		rem[cur+i]=(rem[cur+i]^div[i]);
		while(rem[cur]==0&&cur!=size-1)
		cur++;
		if((size-cur)<size)
		break;
	}
	for(i=0;i<size;i++)
	crc[i]=(div[i]^rem[i]);
	printf("CRC code : ");
	for(i=0;i<size;i++);
	printf("%d ",crc[i]);
	printf("\n");
}
void detection(int length,int div[100])
{
	int crc[100],rem[100],i,cur=0;
	printf("Enter the CRC code at receiver side : ");
	for(i=0;i<length;i++)
	scanf("%d ",&crc[i]);
	printf("\n");
	for(i=0;i<length;i++)
	rem[i]=crc[i];
    while(1)
	{
		for(i=0;i<length;i++)
		rem[cur+i]=(rem[cur+i]^div[i]);
		while(rem[cur]==0&&cur!=length-1)
		cur++;
		if((length-cur)<length)
		break;
	}
	for(i=0;i<length;i++)
	{
		if(rem[i]!=0)
		{   
			printf("Error");
			break;
		}
		if(i==length-1)
		printf("No Error");
	}
}
