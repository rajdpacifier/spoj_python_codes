def binary(n):
    low,mid=0,0
    high=10000000;
    while(low<high):
        mid=(low+high)/2
        k=mid*mid+mid+2
    
        if(k>=n):
            high=mid
        else:
            low=mid+1;
    return low


def main():
    for _ in range(int(input())):
        pi=binary(2*int(input()))
        print(int(pi))

main()