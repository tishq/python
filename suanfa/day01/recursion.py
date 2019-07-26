def fbn(n):
    if(n==1 or n==2):
        return 1
    else:
        return fbn(n-1)+fbn(n-2)
print(fbn(3))