#include<stdio.h>
void fib(int n,int n1,int n2)
{
    if (n <= 0){
        return;
    }
    printf("%d ",n1);
    fib(n-1,n2,n1+n2);
}
int main(){
    int num;
    printf("Enter a num: ");
    scanf("%d",&num);
    fib(num,0,1);
}

