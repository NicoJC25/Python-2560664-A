def potenciador(i,n,x):
    if n==1 or n==0 or n<0:
        return False
    elif i**n==x:
        return True
    else:
        return False

print(potenciador(5,0,25))