#fibonacci series..
"""0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,.. """

n = int(input("enter the number of fibonacci no.s to be printed: "))



def fibo(n):
    if(n==0):
        return 0
    
    if(n==1):
        return 1

    else:
        return fibo(n-1)+fibo(n-2)

i=0
while(i!=n):
    
    print(fibo(i),end=" ")
    i=i+1
    
    
    
    