x=int(input("Ingresar un numero natural: "))
cp=0
ci=0
while x>0:
    r=x%10
    if r % 2==0: #par
        cp=cp+1
    else:
        ci=ci+1
    x=x//10
print("Cantidad de digitos pares:",cp)
print("Cantidad de digitos impares:",ci)
