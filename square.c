#include<stdio.h>
void main()
{
    int i=0;int j,d;
    int sum=0;
    int arr[100];
    scanf("%d",&d);
    while(d>0)
    {
        j=d%10;
       arr[i]=j;
        d=d/10;
        i++;
    }
    
   for(j=0;j<i;j++)
   {
       sum=sum+(arr[j]*arr[j]);
   }
    printf("%d",sum);
    
}