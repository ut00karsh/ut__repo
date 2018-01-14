#include<stdio.h>
#include<math.h>
void ascsort( int array[],int n)
{
    int i,j,temp;
        for (i = 0; i < n; i++)
 {
for (j = 0; j < (n- i- 1); j++)
{
if (array[j] < array[j + 1])
{
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;

            }} }
  }
void main()
{
    int sum=0;
    int arr[50],arr2[50];
    int i=0,j;
    int k=0;
    int d,n;
    scanf("%d",&d);
    scanf("%d",&n);
    
       while(d>0)
    {
        j=d%10;
       arr[i]=j;
        d=d/10;
        i++;
    }
    for(j=n;j<i;j++)
    {
        arr2[k]=arr[j];
        k++;
    }
    
    ascsort(arr2,k);
        
    for(i=0;i<k;i++)
    {
        sum=sum+(arr2[i]*pow(10,i));
    }
                 
   printf("%d",sum); 
    
}