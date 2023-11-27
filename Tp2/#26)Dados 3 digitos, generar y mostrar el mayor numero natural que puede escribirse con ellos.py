a=int(input("Ingresar un numero natural A: "))
b=int(input("Ingresar un numero natural B: "))
c=int(input("Ingresar un numero natural C: "))
if a>b:
    if b>c:
        n1=a
        n2=b
        n3=c
    else:
        n1=c
        n2=a
        n3=b
else:
    n1=c
    n2=a
    n3=b
else:
    if b>c:
        if a>c:
            n1=b
            n2=a
            n3=c
    else:
        n1=b
        n2=c
        n3=a
else:
    n1=c
    n2=b
    n3=a
resultado=n1*100+n2*10+n3
print(resultado)