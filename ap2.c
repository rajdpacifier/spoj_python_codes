#include <stdio.h>
#include<math.h>

int main(void) {
        // your code here
int x,i;
scanf("%d",&x);
for(i=0;i<x;i++)
{       
        long long int sum,n,a,d,l,f;
        
        scanf("%lld %lld %lld",&f,&l,&sum);
        n=(sum*2)/(l+f);
        printf("%lld\n",n);
        d=((l-f)/(n-5));
        a=(f-(2*d));

        for(i=0;i<n;i++)
        {

long long int z=(a+(i*d));
                printf("%lld ",z);
        }
}
return 0;
}