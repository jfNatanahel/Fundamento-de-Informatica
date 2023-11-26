a=int(input("Ingresar numero natural A: ")) 
b=int(input("Ingresar un numero natural B: "))
c=int(input("Ingresar un numero natural C: "))
multiplos=1
divisores=1
bandera=0
while bandera==0:
    if a*multiplos<b and a*multiplos%divisores==0:
        print(multiplos)
    else:
        bandera=1
    multiplos+=1
    divisores+=1
    